from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import Category, Product


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
