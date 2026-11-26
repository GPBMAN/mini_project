from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.decorators.http import require_POST
from .models import Product, UserProfile
from .forms import UserProfileForm
from .cart import Cart


class CustomLoginView(LoginView):
    template_name = 'login.html'


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def allProducts(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'all_products.html', context)


def detailedProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'detailed_product.html', context)


@login_required
def profileView(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        "profile": profile
    }
    return render(request, 'profile.html', context)


@login_required
def editProfile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})


def cartDetail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


@require_POST
def cartAdd(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override') == 'True'
    cart.add(product=product, quantity=quantity, override_quantity=override)
    return redirect('cart_detail')


@require_POST
def cartRemove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('cart_detail')