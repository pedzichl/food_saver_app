from django.shortcuts import render, redirect
from django.views import View
from .forms import AddProductForm
from .models import Product, ProductUser
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
            current_user = request.user.username
            user_db = User.objects.get(username=current_user)
            name = form.cleaned_data ['name']
            expiration_date = form.cleaned_data ['expiration_date']
            quantity = form.cleaned_data ['quantity']
            unit = form.cleaned_data ['unit']
            type = int(form.cleaned_data ['type'])
            image = form.cleaned_data['image']
            new_product = Product.objects.create(name=name, expiration_date=expiration_date,
                                                 quantity=quantity, unit=unit,type=type, image=image, user=user_db)

            assign_to_user = ProductUser.objects.create(product=new_product, user=user_db)
            return redirect('single-product', id=new_product.id)



class ProductsList(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products-list.html", context={"products":products,
                                                              })

class SingleProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        get_user = User.objects.get(username=request.user.username)
        username = ProductUser.objects.get(product=product.id)

        return render(request, "product-details.html", context={"product":product,
                                                                "username": username})

class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', { 'form': UserRegisterForm() })

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
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
        user = User.objects.get(username=current_user)
        get_products = ProductUser.objects.filter(user=user.id)
        product_ids = []
        for product_id in get_products:
            product_ids.append(product_id.product_id)
        products = Product.objects.filter(id__in=product_ids)


        return render(request, 'user-products.html', context={'products': products})

    def post(self, request):
        items_to_delete = request.POST.getlist('delete')
        Product.objects.filter(pk__in=items_to_delete).delete()
        current_user = request.user.username
        user = User.objects.get(username=current_user)
        get_products = ProductUser.objects.filter(user=user.id)
        product_ids = []
        for product_id in get_products:
            product_ids.append(product_id.product_id)
        products = Product.objects.filter(id__in=product_ids)
        return render(request, 'user-products.html', context={'products': products})



class GetProductsView(View):
    def get(self, request):
        current_user = request.user.username
        user = User.objects.get(username=current_user)
        get_products = ProductUser.objects.exclude(user=user.id)
        product_ids = []
        for product_id in get_products:
            product_ids.append(product_id.product_id)
        products = Product.objects.filter(id__in=product_ids)

        return render(request, 'get-products.html', context={'products': products})

    def post(self, request):
        current_user = request.user.username
        user = User.objects.get(username=current_user)
        product_to_get = request.POST.getlist('get')
        get_products = ProductUser.objects.exclude(user=user)
        product_ids = []
        for product_id in get_products:
            product_ids.append(product_id.product_id)
        products = Product.objects.filter(id__in=product_ids)
        ProductUser.objects.filter(product_id__in=product_to_get).update(user_id=user)


        return render(request, 'get-products.html', context={'products': products})


