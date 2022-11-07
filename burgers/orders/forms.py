from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['fio', 'email', 'address', 'phone', 'pickup', 'payment_method']

