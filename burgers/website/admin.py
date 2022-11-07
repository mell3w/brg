from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import MainMenu, Topping, DishesForOrder, ExtraMenu, ToppingForOrder
# Register your models here.

class MainMenuAdmin(admin.ModelAdmin):
    list_display = ['name','img','category', 'compound','price','slug']
    list_display_links = ['name','img','category', 'compound','price', 'slug']
    fields = ['name','img','category', 'compound','price', 'slug']
    search_fields = ['name','category','compound','price', 'slug']

    def img_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='60' />".format(obj.img.url))

    img_show.__name__ = "Фото"


class ExtraMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'category', 'description', 'amount', 'weight', 'price', 'slug']
    list_display_links = ['name', 'img', 'category', 'description', 'amount', 'weight', 'price', 'slug']
    fields = ['name', 'img', 'category', 'description', 'amount', 'weight', 'price', 'slug']
    search_fields = ['name','category', 'description', 'amount', 'weight', 'price', 'slug']

    def img_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='60' />".format(obj.img.url))

    img_show.__name__ = "Фото"




class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name', 'price']
    fields = ['name', 'price']
    search_fields = ['name']

class DishesForOrderAdmin(admin.ModelAdmin):
    list_display = ['dishes', 'price']
    list_display_links = ['dishes', 'price']
    fields = ['dishes','toppings', 'price']
    search_fields = ['dishes','toppings', 'price']


class ToppingForOrderAdmin(admin.ModelAdmin):
    list_display = ['topping','amount', 'price']
    list_display_links = ['topping','amount', 'price']
    fields = ['topping','amount', 'price']
    search_fields = ['topping']



admin.site.site_header = '1137 BURGERS'
admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(ExtraMenu, ExtraMenuAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(DishesForOrder, DishesForOrderAdmin)
admin.site.register(ToppingForOrder, ToppingForOrderAdmin)