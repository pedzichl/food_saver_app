"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from food_saver.views import HomeView, AddProduct, ProductsList, SingleProductView, SignUpView, ProfileView, \
    UsersProductsView, GetProductsView, UserSavedProductsView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('add_product/', login_required(AddProduct.as_view()), name='add-product'),
    path('products_list/', ProductsList.as_view(), name='products-list'),
    path('product/<int:id>/', SingleProductView.as_view(), name='single-product'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', login_required(ProfileView.as_view()), name='user-profile'),
    path('my_products/', login_required(UsersProductsView.as_view()), name='user-products'),
    path('get_products/', login_required(GetProductsView.as_view()), name='get-products'),
    path('saved_products/', login_required(UserSavedProductsView.as_view()), name='saved-products'),

    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
