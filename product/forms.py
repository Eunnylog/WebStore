from django import forms

class ProductForm(forms.Form):
    code = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20, widget=forms.Textarea)
    price = forms.IntegerField()
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = forms.ChoiceField(choices=sizes)