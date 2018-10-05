from django.shortcuts import render
from .models import Product
# Create your views here.

def productView(request):
    obj = Product.objects.all()
    context = {
        "objects_all" : obj,
    }
    return render(request,"products/product_list.html",context)
