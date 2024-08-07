from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from .forms import SignUpForm, UpdateUserForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from .models import Category, Product, Profile
import json


def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'bedding_store/category.html', {'products': products, 'category': category})
    except:
        messages.error(request, 'Такої категорії не існує!')
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'bedding_store/product.html', {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, 'bedding_store/home.html', {'products': products})


def about(request):
    return render(request, 'bedding_store/about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Do some shopping cart stuff
            current_user = Profile.objects.get(user__id=request.user.id)
            # Get their saved cart from database
            saved_cart = current_user.old_cart
            if saved_cart:
                # Convert to Python dictionary using json
                converted_cart = json.loads(saved_cart)
                # Add the loaded cart dictionary to our session
                # Get the cart
                cart = Cart(request)
                # Loop through the cart and add the items from the database
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, 'Ви успішно увійшли до облікового запису!')
            return redirect('home')
        else:
            messages.error(request, 'Помилка авторизації! Спробуйте ще раз!')
            return redirect('login')
    else:
        return render(request, 'bedding_store/login.html', {})


def logout_user(request):
    logout(request)
    messages.warning(request, 'Ви вийшли з облікового запису! Дякуємо за увагу до нашої крамниці!')
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Ви успішно зареєструвалися! Ласкаво просимо!')
            return redirect('home')
        else:
            messages.error(request, 'Помилка реєстрації. Спробуйте ще')
            return redirect('register')
    return render(request, 'bedding_store/register.html', {'form': form})


def update_info(request):
    if request.user.is_authenticated:
        #  Get current user
        current_user = Profile.objects.get(user__id=request.user.id)
        #  Get current user's shipping info
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, 'Вашу інформацію було оновлено!')
            return redirect('home')
        return render(request, 'bedding_store/update_info.html', {'form': form, 'shipping_form': shipping_form})
    else:
        messages.error(request, 'Увійдіть у Ваш обліковий запис!')
        return redirect('login')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = PasswordChangeForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ваш пароль успішно змінено!')
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    login(request, current_user)
                    return redirect('update_user')
        else:
            form = PasswordChangeForm(current_user)
            return render(request, 'bedding_store/update_password.html', {'form': form})
    else:
        messages.error(request, 'Увійдіть у Ваш обліковий запис!')
        return redirect('login')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'Ваш обліковий запис успішно оновлено!')
            return redirect('home')
        return render(request, 'bedding_store/update_user.html', {'user_form': user_form})
    else:
        messages.error(request, 'Увійдіть у Ваш обліковий запис!')
        return redirect('home')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # Querying the Products DB model
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.error(request, 'Цей продукт не існує. Спробуйте ще..')
            return render(request, 'bedding_store/search.html', {})
        else:
            return render(request, 'bedding_store/search.html', {'searched': searched})
        return render(request, 'bedding_store/search.html', {'searched': searched})
    else:
        return render(request, 'bedding_store/search.html', {})
