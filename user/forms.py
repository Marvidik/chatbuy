from django import forms 
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput,EmailInput,Select,NumberInput,IntegerField
from .models import Vendor



class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

        widgets = {
            'username': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
            'email': EmailInput(attrs={ 'id': 'email', 'type':"email" ,'name':"email"}),
            'password': PasswordInput(attrs={ 'id': 'pass', 'placeholder': 'Password','type':"password" ,'name':"pass"}),
            'first_name': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
            'last_name': TextInput(attrs={ 'id': 'name', 'type':"text" ,'name':"name"}),   
        }

class VendorForm(forms.ModelForm):
   
    class Meta:
        model=Vendor
        fields= ['bussiness_name','bussiness_address','phone_number','Cac','nearest_landmark','lga','state']

        widgets={
             'bussiness_name': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'bussiness_address': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'phone_number': NumberInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'Cac': NumberInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'nearest_landmark': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'lga': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'state': Select(attrs={'id': 'name', 'type':"text" ,'name':"name"}),




        }