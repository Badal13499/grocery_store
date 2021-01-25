from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Item_data


class DataForm(forms.ModelForm):
    class Meta:
        model = Item_data
        fields = ('item_name', 'item_quantity', 'item_status', 'date')