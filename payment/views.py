from django.shortcuts import redirect, render
from cart.cart import Cart
from django.contrib import messages
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quantity
        totals = cart.cart_total()

        # Check to see if user is logged in
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_inf": request.POST, "billing_form": billing_form})
        
        else:
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_inf": request.POST, "billing_form": billing_form})

        
    else:
         messages.success(request, 'Зареєструйтесь або увійдіть у Ваш обліковий запис')
         return redirect('home')
         


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quantity
    totals = cart.cart_total()

    if request.user.is_authenticated:
		# Checkout as logged in user
		# Shipping User
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		# Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    


def payment_success(request):

	return render(request, "payment/payment_success.html", {})
