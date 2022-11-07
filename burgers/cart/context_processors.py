from .cart import Cart
from django.shortcuts import render

def cart_detail(request):
    cart=Cart(request)

    return render(request, 'cart/detail.html', {'cart':cart})