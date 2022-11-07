from django.db import models
from django.db.models import Sum

class Topping(models.Model):
    name = models.CharField(max_length=300, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name='Добавка'
        verbose_name_plural = 'Добавки'

    def __str__(self):
        return f'{self.name}'

class MainMenu(models.Model):
    BURGERS = 'Бургеры'
    SHWARMA = 'Шаверма/Роллы'
    KEBAB = 'Шашлык'
    DRINKS = 'Напитки'
    SNACKS = 'Закуски'
    SAUCES = 'Соусы'
    CHOICE_GROUP = {
        (BURGERS, 'Бургеры'),
        (SHWARMA, 'Шаверма/Роллы'),
        (KEBAB, 'Шашлык'),
        (DRINKS, 'Напитки'),
        (SNACKS, 'Закуски'),
        (SAUCES, 'Соусы')
    }
    name = models.CharField(max_length=300, verbose_name='Наименование')
    img = models.ImageField(default='no_image.jpg', upload_to='dishes_image' )
    category = models.CharField(max_length=300, choices=CHOICE_GROUP, verbose_name='Категория')
    compound = models.CharField(max_length=700, null=True, blank=True, verbose_name='Состав')
    amount = models.IntegerField(null=True, blank=True, verbose_name='Количество')
    weight = models.IntegerField(null=True, blank=True, verbose_name='Вес, г')
    price = models.IntegerField(default=0,verbose_name='Цена')
    slug = models.CharField(max_length=100, verbose_name='Ссылка')


    class Meta:
        verbose_name = 'Основное меню'
        verbose_name_plural = 'Основное меню'

    def __str__(self):
        return f'{self.name}'


class ToppingForOrder(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0,verbose_name='Цена')
    def save(self, *args, **kwargs):
        self.price = Topping.objects.get(name=self.topping).price * self.amount
        super().save(args, kwargs)

    class Meta:
        verbose_name = 'Топинг для заказа'
        verbose_name_plural = 'Топинги для заказов'
    def __str__(self):
        return f'{self.topping} - {self.amount}'


class DishesForOrder(models.Model):
    dishes = models.ForeignKey(MainMenu,on_delete=models.CASCADE)
    toppings = models.ManyToManyField(ToppingForOrder)
    price = models.IntegerField(default=0, verbose_name='Цена')

    #def save(self, *args, **kwargs):
    #    #self.price = self.dishes.price + ToppingForOrder.objects.aggregate(Sum('price')).get('price__sum')
    #    self.price = self.dishes.price
    #    super().save(args, kwargs)

    class Meta:
        verbose_name = 'Блюдо для заказа'
        verbose_name_plural = 'Блюда для заказов'

    def __str__(self):
        return f'{self.dishes.name}'



class ExtraMenu(models.Model):
    KEBAB = 'Шашлык'
    DRINKS = 'Напитки'
    SNACKS = 'Закуски'
    SAUCES = 'Соусы'
    CHOICES_CATEGORY = {
        (KEBAB, 'Шашлык'),
        (DRINKS, 'Напитки'),
        (SNACKS, 'Закуски'),
        (SAUCES, 'Соусы')
    }
    name = models.CharField(max_length=300, verbose_name='Наименование')
    category = models.CharField(max_length=300, choices=CHOICES_CATEGORY, verbose_name='Категория')
    img = models.ImageField(default='no_image.jpg', upload_to='dishes_image')
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    amount = models.IntegerField(null=True, blank=True, verbose_name='Количество')
    weight = models.IntegerField(null=True, blank=True,verbose_name='Вес, г')
    price = models.IntegerField(verbose_name='Цена')
    slug = models.CharField(max_length=300, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Второстепенное меню'
        verbose_name_plural = 'Второстепенное меню'

    def __str__(self):
        return f'{self.name}'