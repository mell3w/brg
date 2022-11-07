from django.shortcuts import render
from .models import MainMenu, Topping, ToppingForOrder, DishesForOrder, ExtraMenu
from django.conf import settings
from django.shortcuts import get_object_or_404
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.db.models import Q


# Create your views here.


def index(request):
    cart = Cart(request)
    burger = MainMenu.objects.filter(category='Бургеры')
    topping = Topping.objects.all()
    if request.method == 'POST' and 'add_to_cart' in request.POST:
        brg = MainMenu.objects.get(id=request.POST.get('burgerid'))
        dfo = DishesForOrder()
        dfo.dishes = brg
        dfo.price = brg.price
        dfo.save()
        price_topping = int(0)
        for t in topping:
            top = ToppingForOrder()
            top.topping = t
            top.amount = int(request.POST.get(f'topping_amount{t.id}'))
            top.price = int(request.POST.get(f'topping_price{t.id}'))
            top.save()
            dfo.toppings.add(top)
            price_topping = price_topping + top.price


        total_price = dfo.price + price_topping
        dfo.price = total_price
        dfo.save()
        cart_product_form = CartAddProductForm()
        x = dfo.id
        dishesfororder = DishesForOrder.objects.get(id=x)
        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add_main(dishesfororder=dishesfororder,
                          quantity=cd['quantity'],
                          update_quantity=cd['update'])


    else:
        cart_product_form = CartAddProductForm()
        dishesfororder = DishesForOrder.objects.get(id=1)

    if request.method == 'POST' and 'extra_add' in request.POST:
        extramenu = ExtraMenu.objects.get(id=request.POST.get('extra_id'))
        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add_extra(extramenu=extramenu,
                           quantity=cd['quantity'],
                           update_quantity=cd['update'])

    context = {'burger': burger, 'topping': topping, 'cart_product_form': cart_product_form,
               'dishesfororder': dishesfororder, 'cart':cart}
    return render(request, 'website/index.html', context)


def menu(request):
    cart = Cart(request)
    extra = MainMenu.objects.filter(Q(category='Шашлык')|Q(category='Закуски'))
    burger = MainMenu.objects.filter(category='Бургеры')
    drinks = MainMenu.objects.filter(category='Напитки')
    sauces = MainMenu.objects.filter(category='Соусы')
    topping = Topping.objects.all()


    if request.method == 'POST' and 'sauces_add' in request.POST:
        sous = MainMenu.objects.get(id=request.POST.get('sauces_id'))
        dfo = DishesForOrder()
        dfo.dishes = sous
        dfo.price = sous.price

        dfo.save()
        cart_product_form = CartAddProductForm()
        x = dfo.id
        dishesfororder = DishesForOrder.objects.get(id=x)

        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add_main(dishesfororder=dishesfororder,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        context = {'burger': burger, 'topping': topping, 'cart_product_form': cart_product_form,
                   'dishesfororder': dishesfororder, 'extra': extra,'drinks':drinks, 'sauces':sauces, 'cart':cart}
    if request.method == 'POST' and 'drinks_add' in request.POST:
        beverages = MainMenu.objects.get(id=request.POST.get('drinks_id'))
        dfo = DishesForOrder()
        dfo.dishes = beverages
        dfo.price = beverages.price

        dfo.save()
        cart_product_form = CartAddProductForm()
        x = dfo.id
        dishesfororder = DishesForOrder.objects.get(id=x)

        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add_main(dishesfororder=dishesfororder,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        context = {'burger': burger, 'topping': topping, 'cart_product_form': cart_product_form,
                   'dishesfororder': dishesfororder, 'extra': extra,'drinks':drinks, 'sauces':sauces, 'cart':cart}

    if request.method == 'POST' and 'extra_add' in request.POST:
        extramenu = MainMenu.objects.get(id=request.POST.get('extra_id'))
        dfo = DishesForOrder()
        dfo.dishes = extramenu
        dfo.price = extramenu.price

        dfo.save()
        cart_product_form = CartAddProductForm()
        x = dfo.id
        dishesfororder = DishesForOrder.objects.get(id=x)

        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add_main(dishesfororder=dishesfororder,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        context = {'burger': burger, 'topping': topping, 'cart_product_form': cart_product_form,
                   'dishesfororder': dishesfororder, 'extra': extra,'drinks':drinks, 'sauces':sauces, 'cart':cart}
    if request.method == 'POST' and 'add_to_cart' in request.POST:
        brg = MainMenu.objects.get(id=request.POST.get('burgerid'))
        dfo = DishesForOrder()
        dfo.dishes = brg
        dfo.price = brg.price
        dfo.save()
        price_topping = int(0)
        topping_list = []
        for t in topping:
            top= ToppingForOrder()
            top.topping = t
            top.amount = int(request.POST.get(f'topping_amount{t.id}'))
            top.price = int(request.POST.get(f'topping_price{t.id}'))
            top.save()
            dfo.toppings.add(top)
            price_topping = price_topping + top.price
            print(top.id)
            for_top_list = (top.topping,top.amount)
            topping_list.append(for_top_list)
            print(top.topping)


        print(topping_list)
        total_price = dfo.price + price_topping
        dfo.price = total_price
        dfo.save()
        cart_product_form = CartAddProductForm()
        x = dfo.id
        dishesfororder = DishesForOrder.objects.get(id=x)

        cart=Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add_main(dishesfororder=dishesfororder,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        context = {'burger': burger, 'topping': topping, 'cart_product_form': cart_product_form,
                   'dishesfororder': dishesfororder, 'extra': extra,'drinks':drinks, 'sauces':sauces, 'topping_list':topping_list, 'cart':cart}




    else:
        topping_list=[]
        cart_product_form = CartAddProductForm()
        dishesfororder = DishesForOrder.objects.get(id='2')
        context = {'burger': burger, 'topping': topping, 'cart_product_form': cart_product_form, 'extra': extra,
                   'dishesfororder': dishesfororder,'drinks':drinks, 'sauces':sauces, 'topping_list':topping_list, 'cart':cart}









    return render (request, 'website/menu.html', context)