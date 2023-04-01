from django.shortcuts import redirect, render
from .forms import UserCreationForm,VendorForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic  import CreateView
from django.contrib.auth.models import User 
from .models import Vendor,Notification
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from products.models import Order,Products
from django.contrib.auth import logout
from .decorators import group_required
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404


# Create your views here.

def all_reg(request):
    if request.method == 'POST' and 'userf' in request.POST:
        uform = UserCreationForm(request.POST)
        if uform.is_valid():
            # Hash the password
            password = make_password(uform.cleaned_data['password'])
            
            # Create the new user with hashed password
            user = uform.save(commit=False)
            user.password = password
            user.save()

            # Add the user to the 'customer' group
            customer_group = Group.objects.get(name='customer')
            customer_group.user_set.add(user)
   
        return redirect('login')
    elif request.method == 'POST' and 'vendorf' in request.POST:
        vform = VendorForm(request.POST)
        if vform.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            new_user = User.objects.create_user(username=username, email=email, password=password)

            vendors_group = Group.objects.get(name='vendor')
            new_user.groups.add(vendors_group)

            vform.instance.user = new_user
            vform.save()
            return redirect('login')
    else:
        uform = UserCreationForm()
        vform = VendorForm()

    return render(request, 'user/signup.html', {'uform': uform, 'vform': vform})


class Login(LoginView):
    template_name="user/login.html"


def logoutuser(request):
    logout(request)
    return redirect('/')

def forget_password(request):


    return render(request,"user/forgetPassword.html")

@login_required
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "user/message.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("user/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="user/forgetPassword.html", context={"password_reset_form":password_reset_form})



@login_required
@group_required(groups=['vendor'])
def vendor_dashboard(request):
    order_items = Order.objects.filter(store=request.user.vendor_set.all()[0])
    total=order_items.count

    user = request.user
    vendor = Vendor.objects.get(user=user)
    image = vendor.image



    prod=Products.objects.filter(store_name=request.user.vendor_set.all()[0])
    ptotal=prod.count
    
    context={"order_items":order_items,"total":total,"ptotal":ptotal,"image":image}

    return render (request,"user/VendorAdmin.html",context)



@login_required
@group_required(groups=['customer'])
def customer_dashboard(request):
      order_items = Order.objects.filter(user=request.user)
      
      context={"order_items":order_items}
      return render(request, "user/customerAdmin.html",context)

@login_required
def notification(request):
      notification = Notification.objects.filter(user=request.user)
      context={"notification":notification}

      return render(request,"user/notifications.html",context)


@login_required
@group_required(groups=['super'])
def super_user(request):
      prod=Products.objects.all()
      ptotal=prod.count

      order = Order.objects.all()

      order_items = Order.objects.all()
      total=order_items.count

      products=Products.objects.filter(status="Disabled")

      aproducts=Products.objects.filter(status="Active")

      vendors=Vendor.objects.all()

      vendor_group = Group.objects.get(name='vendor')
      vendor_users_count = User.objects.filter(groups=vendor_group).count()

      customer_group = Group.objects.get(name='customer')
      customer_users_count = User.objects.filter(groups=customer_group).count()
      
      context={"order":order,"total":total,"ptotal":ptotal,"products":products,"aproducts":aproducts,"vendors":vendors,"vendor_users_count":vendor_users_count,"customer_users_count":customer_users_count}

      

      return render(request,"user/superAdmin.html",context)



def update_status(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.status = 'Active'  # replace 'new_status' with the desired status
    product.save()
    return redirect('super')  # redirect to the product detail page


def remove(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete() 
    return redirect('super')



def details(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context={"order":order}
    
    return render(request,"user/vendordetails.html",context)  