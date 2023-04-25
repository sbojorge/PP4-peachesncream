from django import forms
from .models import Grocery


class GroceryForm(forms.ModelForm):
    """
    Form to create a grocery shopping list
    """
    class Meta:
        model = Grocery
        fields = ['name', 'item']
