#from django.shortcuts import render
#
#from django.shortcuts import get_object_or_404
#from cart.forms import CartAddProductForm
#
#def add_to_cart(request):
#    cart_product_form = CartAddProductForm()
#    context = {'cart_product_form':cart_product_form}
#    return (context)
#from cart.context_processors import Cart
#from django.shortcuts import render
#
#def cart_detail(request):
#    cart=Cart(request)
#
#    return render(request, 'cart/detail.html', {'cart':cart})