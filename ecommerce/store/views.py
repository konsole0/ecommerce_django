from django.shortcuts import render
from .models import *

def store(request):
	products = Product.objects.all()
	context = {
		'products': products
	}
	return render(request, 'store/store.html', context)

def cart(request):
	# query the order items
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all() # django automatically generates a set for each table/model that contain a FK for Order table/model 
	else:
		# if the user is guest (not registered)
		items = [] # leave it empty for now
		order = {'getTotal': 0, 'getItemsNumber': 0} # for prevent an error if we are logged out now

	context = {
		'items': items,
		'order': order
	}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)