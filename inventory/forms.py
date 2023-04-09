from django import forms

class InventoryForm(forms.Form):

    total_quantity = forms.IntegerField()