# Generated by Django 3.2.11 on 2022-09-01 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20220829_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishesForOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Блюдо для заказа',
                'verbose_name_plural': 'Блюда для заказа',
            },
        ),
        migrations.CreateModel(
            name='ExtraMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('category', models.CharField(choices=[('Шашлык', 'Шашлык'), ('Напитки', 'Напитки'), ('Закуски', 'Закуски'), ('Соусы', 'Соусы')], max_length=300, verbose_name='Категория')),
                ('img', models.ImageField(default='no_image.jpg', upload_to='dishes_image')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Вес, г')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Второстепенное меню',
                'verbose_name_plural': 'Второстепенное меню',
            },
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('img', models.ImageField(default='no_image.jpg', upload_to='dishes_image')),
                ('category', models.CharField(choices=[('Бургеры', 'Бургеры'), ('Шаурма', 'Шаурма')], max_length=300, verbose_name='Категория')),
                ('compound', models.CharField(max_length=700, verbose_name='Состав')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('slug', models.CharField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Основное меню',
                'verbose_name_plural': 'Основное меню',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Добавка',
                'verbose_name_plural': 'Добавки',
            },
        ),
        migrations.DeleteModel(
            name='Burger',
        ),
        migrations.AddField(
            model_name='dishesfororder',
            name='dishes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.mainmenu'),
        ),
        migrations.AddField(
            model_name='dishesfororder',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, to='website.Topping'),
        ),
    ]