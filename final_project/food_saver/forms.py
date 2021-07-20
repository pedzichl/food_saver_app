from django import forms
from food_saver.models import Product, DIET_TYPE, UNITS_CHOICES, Category, CATEGORIES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AddProductForm(forms.Form):
    name = forms.CharField(label="Product's name")
    expiration_date = forms.DateField(label="Expiration date", widget=forms.SelectDateWidget())
    quantity = forms.IntegerField(label="Quantity", min_value=1)
    unit = forms.ChoiceField(label="Unit", choices= UNITS_CHOICES)
    type = forms.ChoiceField(label="Diet Type", choices= DIET_TYPE)
    image = forms.ImageField(label="Image", required=False, widget=forms.FileInput)

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phone = forms.IntegerField(min_value=100000000)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput, max_length=64)

class CategoryForm(forms.Form):
    category_name = forms.ChoiceField(label="Category name", choices=CATEGORIES)

