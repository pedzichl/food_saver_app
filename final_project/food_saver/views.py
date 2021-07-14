from django.shortcuts import render, redirect
from django.views import View
from .forms import AddProductForm
from .models import Product, ParticularUser, ProductParticularUser
from django.contrib.auth.models import User
from django.views import generic, View
from .forms import UserRegisterForm

# Create your views here.


class HomeView(View):
    def get(self, request):
        count = User.objects.count()
        return render(request, "home.html", {'count': count})

class AddProduct(View):
    def get(self, request):
            form = AddProductForm()
            return render(request, "add-product.html", {'form': form})

    def post(self, request):
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data ['name']
            expiration_date = form.cleaned_data ['expiration_date']
            quantity = form.cleaned_data ['quantity']
            unit = form.cleaned_data ['unit']
            type = int(form.cleaned_data ['type'])
            image = form.cleaned_data ['image']
            new_product = Product.objects.create(name=name, expiration_date=expiration_date,
                                                 quantity=quantity, unit=unit,type=type, image=image)
            current_user = request.user.username
            user_db = ParticularUser.objects.get(username=current_user)
            assign_to_user = ProductParticularUser.objects.create(product=new_product, user=user_db)
            return redirect('single-product', id=new_product.id)



class ProductsList(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products-list.html", context={"products":products,
                                                              })

class SingleProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        get_user = ParticularUser.objects.get(username=request.user.username)
        username = ProductParticularUser.objects.get(product=product.id)

        return render(request, "product-details.html", context={"product":product,
                                                                "username": username})

class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', { 'form': UserRegisterForm() })

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data ['username']
            email = form.cleaned_data ['email']
            first_name = form.cleaned_data ['first_name']
            last_name = form.cleaned_data ['last_name']
            new_user_db = ParticularUser.objects.create(username=username, email=email, first_name=first_name,last_name=last_name)
            user = form.save()
            return redirect(('login'))

        return render(request, 'registration/signup.html', { 'form': form })

class ProfileView(View):
    def get(self, request):
        current_user = request.user
        return render(request, 'profile.html', context={'user' : current_user})

class UsersProductsView(View):
    def get(self, request):
        current_user = request.user.username
        user = ParticularUser.objects.get(username=current_user)
        get_products = ProductParticularUser.objects.filter(user=user.id)
        id_products = []
        for p in get_products:
            id_products.append(p.id)
        products = Product.objects.filter(id_products=id_products)



        return render(request, 'user-products.html', context={'products': tuple_id_products})


# class GetProductsView(View):
#     def get(self, request):
#         current_user = request.user.username
#         user = ParticularUser.objects.get(username=current_user)
#         return render(request, 'get-products.html', context={'products': products})


