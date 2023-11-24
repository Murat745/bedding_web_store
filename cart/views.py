from django.shortcuts import get_object_or_404, render
from .cart import Cart
from bedding_store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
