from django.conf import settings
from website.models import DishesForOrder

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_main(self, dishesfororder, quantity=1, update_quantity=False):
        product_id = str(dishesfororder.id)
        if product_id not in self.cart:
            self.cart[product_id]={
                'quantity':0,
                'price':str(dishesfororder.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID]=self.cart
        self.session.modified = True

    def remove_main(self, dishesfororder):
        product_id = str(dishesfororder.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        product_ids = self.cart.keys()
        #try:
        #    products = DishesForOrder.objects.filter(id__in=product_ids)
        #except:
        #    products = ExtraMenu.objects.filter(id__in=product_ids)

        products = DishesForOrder.objects.filter(id__in=product_ids)


        print(products)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
