from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Products,Cart,Order
from django.shortcuts import redirect, render,get_object_or_404
from .forms import ProductForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from user.decorators import group_required

# Create your views here.

def products(request):
    prod=Products.objects.filter(status="Active")
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user, ordered=False)
        if not cart_items:
            pass

    # Calculate the total cost of the order
    if request.user.is_authenticated:
        total_cost = sum(cart_item.quantity * cart_item.product.price for cart_item in cart_items)


        carts=Cart.objects.filter(user=request.user,ordered=False)
        context={'products':prod,'carts':carts,'total_cost':total_cost}
    else:
        context={'products':prod}

    


    return render(request,"products/indexE.html",context)


@login_required
@group_required(groups=['vendor'])
def admin_dashboard(request):
    products=Products.objects.all()
    form=form = ProductForm()

    vendor=request.user.vendor_set.all()[0]

    prod=Products.objects.filter(store_name=vendor)

    context={'products':products,"pform":form,"prod":prod}


    return render (request,"products/products.html",context)

@login_required
@group_required(groups=['vendor'])
def add_product(request):
    if request.method=='POST' and 'addproduct' in request.POST:
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            # Create a new instance of the Product model using the form data
            p = form.save(commit=False)
            # Set the store_name field to the currently logged-in vendor
            
            p.status="Disabled"
            p.sales=1
            p.store_name = request.user.vendor_set.all()[0]
            # Save the new product to the database
            p.save()
            form.save()
            return redirect("dash")
            
            
        else:
            print("so many issues")
    else:
        form = ProductForm()
    return HttpResponseRedirect(reverse("dash"))

@login_required
def product_delete(request,id):
    obj=get_object_or_404(Products,pk=id)
    obj.delete()
    return redirect("dash")



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'products/update.html'
    success_url = reverse_lazy('dash')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uform'] = self.get_form()
        return context



    
class SearchResultsView(LoginRequiredMixin, ListView):
    model = Products
    template_name = "products/products.html"
    context_object_name = "prod"

    def get_queryset(self):
        query = self.request.GET.get("q")
        user = self.request.user
        vendor = user.vendor_set.all()[0].id
       
        object_list = Products.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query) ,store_name=vendor
        )

        if object_list:
            return object_list
        else:
            return redirect('home')
        
        
class HomeResultsView(ListView):
    model = Products
    template_name = "products/indexE.html"
    context_object_name="products"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Products.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query) 
        )

        if object_list:
            return object_list
        else:
            return redirect('home')
    

@login_required
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
        quantity=1,
        store=product.store_name
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('dash')



@login_required
def increment(request,cart_id):
    cart_item=get_object_or_404(Cart, id=cart_id,user=request.user,ordered=False)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('home')

@login_required
def decrement(request,cart_id):
    cart_item=get_object_or_404(Cart, id=cart_id,user=request.user,ordered=False)
    cart_item.quantity -=1
    cart_item.save()
    return redirect('home')




@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user, ordered=False)
    if not cart_items:
        messages.warning(request, "Your cart is empty.")
        return redirect('home')

    total_cost = sum(cart_item.quantity * cart_item.product.price for cart_item in cart_items)

    if request.method == 'POST':
        shipping_address = request.POST['shipping_address']
        
        # Get the store name from the first cart item
        store_name = cart_items.first().product.store_name
        image=cart_items.first().product.image

        
        

        for cart_item in cart_items:
            order = Order.objects.create(
                image=cart_item.product.image,
                name=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price,
                user=request.user,
                store=store_name,
                shipping_address=shipping_address,
                total_cost=total_cost,
    )

            cart_items.update(ordered=True)

        messages.success(request, "Your order has been placed! Thank you for shopping with us.")
        return redirect('home')

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost,
    }
    return render(request, 'products/checkout.html', context)

