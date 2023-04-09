from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InventoryForm
from .models import InventoryModel
from product.models import ProductModel


def inbound_create(request, id):
    if request.method == 'GET':
        product_id = id
        inventory_form = InventoryForm()
        all_inventory = InventoryModel.objects.filter(author_id=request.user, product_id=product_id)
        inventory_total = 0
        for i in all_inventory:
            inventory_total += i.total_quantity
        return render(request, 'product/inventory.html', {'inventory_form' : inventory_form, 'product' : product_id,
                                                          'all_inventory' : all_inventory, 'total' : inventory_total})
    elif request.method == 'POST':
        user = request.user
        inventory_form = request.POST
        my_inventory = InventoryModel()
        my_inventory.author = user
        my_inventory.product = ProductModel.objects.get(id=id)
        my_inventory.total_quantity = inventory_form['total_quantity']
        my_inventory.save()
        return redirect(f'/inventory/{id}')