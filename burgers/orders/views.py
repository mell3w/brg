from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            list_products = []
            for item in cart:
                OrderItem.objects.create(order=order,
                                               product=item['product'],
                                               price=item['price'],
                                               quantity=item['quantity'])

                topping_item = item['product']
                top_name = topping_item.toppings.all()
                for item in cart:

                    list_products.append(item['product'])

                    for topping in top_name:
                        list_products.append(topping)

                    list_products.append(item['price'])

                    list_products.append(item['quantity'])
                len_list = len(list_products)
                mail_text = str('')
                for x in range(len_list):
                    mail_text = mail_text+str(f'{list_products[x]} \n')
            send_mail(
                f'''Заказ на имя {order.fio}!''',
                f'''{mail_text}''',
                'mirodomgroup@gmai.com',
                ['mirodomgroup@gmail.com'],
                fail_silently=False,
            )


            cart.clear()
            return render(request, 'orders/order/created.html', {'order':order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',  {'cart': cart, 'form': form})
