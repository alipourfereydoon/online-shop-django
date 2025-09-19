from django.shortcuts import render,get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Avg

def product_list(request):
    products = Product.objects.all()
    number_of_products = products.count()
    Avg_rating = products.aggregate(Avg("rating"))
    return render(request,'product_module/product_list.html',context={'products':products , 'total_number_of_products': number_of_products , 'average_rating':Avg_rating})

def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug)
    
    
    return render(request,'product_module/product_detail.html', context={'product':product})
