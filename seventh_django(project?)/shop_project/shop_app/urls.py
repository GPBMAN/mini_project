from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views as v

urlpatterns = [
    path('products/', v.allProducts, name="all_products"),
    path('product/<int:pk>', v.detailedProduct, name="detailed_product"),
    path('profile/', v.profileView, name="profile"),
    path('edit_profile/', v.editProfile, name="edit_profile"),
    path('login/', v.CustomLoginView.as_view(), name="login"),
    path('register/', v.registerView, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cart/', v.cartDetail, name="cart_detail"),
    path('cart/add/<int:pk>', v.cartAdd, name="cart_add"),
    path('cart/remove/<int:pk>', v.cartRemove, name="cart_remove"),
]