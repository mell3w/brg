# Generated by Django 3.2.11 on 2022-08-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20220829_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burger',
            name='add_bacon',
        ),
        migrations.RemoveField(
            model_name='burger',
            name='add_ched',
        ),
        migrations.RemoveField(
            model_name='burger',
            name='add_crispy_onion',
        ),
        migrations.RemoveField(
            model_name='burger',
            name='add_jalapeno',
        ),
        migrations.RemoveField(
            model_name='burger',
            name='add_onion',
        ),
    ]
