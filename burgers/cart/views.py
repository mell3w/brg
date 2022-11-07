from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from website.models import DishesForOrder, ExtraMenu
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.


@require_POST
def cart_add_main(request, dishesfororder_id):
    previous_page = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    dishesfororder = get_object_or_404(DishesForOrder, id=dishesfororder_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_main(dishesfororder=dishesfororder,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect(previous_page)



def cart_remove_main(request, dishesfororder_id):
    previous_page = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    product = get_object_or_404(DishesForOrder, id=dishesfororder_id)
    cart.remove_main(product)
    return redirect(previous_page)



