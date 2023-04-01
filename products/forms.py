from django import forms 
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput,EmailInput,Select,NumberInput,IntegerField,Textarea,ImageField,FileInput
from .models import Products




class ProductForm(forms.ModelForm):
   
    class Meta:
        model=Products
        fields= ['category','name','stock','price','image','description']

        widgets={
             'category': Select(attrs={'id': 'name', 'type':"text" ,'name':"name"}),
             'name': TextInput(attrs={'id': 'name', 'type':"text" ,'name':"name",'placeholder':'product name'}),
             'stock': NumberInput(attrs={'id': 'name', 'type':"number" ,'name':"name",'placeholder':'stock'}),
             'price': NumberInput(attrs={'id': 'name', 'type':"number" ,'name':"name","placeholder":"price"}),
             'description': Textarea(attrs={'id': 'name', 'type':"text" ,'name':"name","placeholder":"description"}),
             'image': FileInput(attrs={'id': 'name', 'type':"file" ,'name':"name"}),


        }