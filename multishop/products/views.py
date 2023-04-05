from django.shortcuts import render
from tkinter import E
from products.models import Product
from django.http import HttpResponseRedirect,HttpResponse

from .models import Product
# Create your views here.

def detail(request, slug):
    context={
    'product': Product.objects.get(slug =slug),
    'featured': Product.objects.filter(featured=True),
    }
#     if product == Product.objects.get(slug =slug)
    return render(request, 'detail.html', context)