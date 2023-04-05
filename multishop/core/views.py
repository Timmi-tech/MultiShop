from django.shortcuts import render
from products.models import Product, Category
# Create your views here.

def index(request):
    context = {
        'products' : Product.objects.filter(active=True),
        'categorys': Category.objects.all(),
        'featured': Product.objects.filter(featured=True),
        'recent_products': Product.objects.filter(recent_products=True),
        'special_offer': Product.objects.filter(special_offer=True),

}
    return render(request, 'index.html', context)


def shop(request):
    context={

    'products' : Product.objects.filter(active=True),
    }
    return render(request, 'shop.html', context)