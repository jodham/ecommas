from django.shortcuts import render
from .models import *
# Create your views here.

#def store(request):
#	products	=	 Product.objects.all()
 #   context	=	{ 'products'	:products }
#	return render(request,	'app/store.html',	context)
def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'app/store.html', context)


def cart(request):
    context = {}
    return render(request, 'app/cart.html',	context)


def checkout(request):
    context = {}
    return render(request, 'app/checkout.html',	context)

