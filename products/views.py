from django.shortcuts import render
from django.views import generic
from .models import Product
# Create your views here.

def productView(request):
    obj = Product.objects.all()
    context = {
        "objects_all" : obj,
    }
    return render(request,"products/product_list.html",context)

class productlistview(generic.ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return Product.objects.all()

def ProductDetailView(request,slug):
    obj = Product.objects.get(slug=slug)
    context ={
        "object" : obj,
    }
    return render(request,"products/Product_detail_view.html",context)
