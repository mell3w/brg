# Generated by Django 3.2.11 on 2022-10-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20221001_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extramenu',
            name='category',
            field=models.CharField(choices=[('Напитки', 'Напитки'), ('Шашлык', 'Шашлык'), ('Соусы', 'Соусы'), ('Закуски', 'Закуски')], max_length=300, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='category',
            field=models.CharField(choices=[('Закуски', 'Закуски'), ('Соусы', 'Соусы'), ('Шаверма/Роллы', 'Шаверма/Роллы'), ('Напитки', 'Напитки'), ('Шашлык', 'Шашлык'), ('Бургеры', 'Бургеры')], max_length=300, verbose_name='Категория'),
        ),
    ]