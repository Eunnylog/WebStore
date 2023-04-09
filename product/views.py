from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import ProductModel

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product')
    else:
        return redirect('/sign-in')


def product_list(request):
    if request.method == 'GET':
        user = request.user
        all_product = ProductModel.objects.filter(author_id=user)
        if user:
            return render(request, 'product/product_list.html', {'product' : all_product})



@login_required
def product_create(request):
    if request.method == 'GET':
        product_form = ProductForm()
        return render(request, 'product/product_create.html', {'product_form' : product_form})
    elif request.method == 'POST':
        user = request.user
        product_form = request.POST
        my_product = ProductModel()
        my_product.author = user
        my_product.code = product_form['code']
        my_product.price = product_form['price']
        my_product.size = product_form['size']
        my_product.description = product_form['description']
        my_product.name = product_form['name']
        my_product.save()
        return redirect('/product_list')