from django.db import models
from website.models import DishesForOrder

# Create your models here.


class Order(models.Model):
    CASH = 'Наличными курьеру'
    CARD = 'Картой/Перевод/СБП'
    CHOICE_GROUP = {
        (CASH, 'Наличными курьеру'),
        (CARD, 'Картой/Перевод/СБП')
    }
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=12, null=True, blank=True, verbose_name='Телефон')
    pickup = models.BooleanField(default=False, verbose_name='Самовывоз')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Заказ создан')
    payment_method = models.CharField(max_length=300, choices=CHOICE_GROUP, verbose_name='Способ оплаты')
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(DishesForOrder, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

