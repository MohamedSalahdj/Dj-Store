from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Product_Images, Brand, Review

def queryset_debug(request):

    # data = Product.objects.all() 
    # data = Product.objects.select_related('brand').all() #=prefetch_related --> M-T-M

    #filter  (> , <, >= , >=)m Range
    # data = Product.objects.select_related('brand').filter(price__gt=1500) # >
    # data = Product.objects.select_related('brand').filter(price__lt=1500) # < 
    # data = Product.objects.select_related('brand').filter(price__gte=2500) # >=
    # data = Product.objects.filter(price__lte=350)

    #navigate relation
    # data = Product.objects.filter(brand__name= 'Samsung')

    #Filter With
    # data = Product.objects.filter(name__contains='Green')
    # data = Product.objects.filter(name__startswith='L')
    # data = Product.objects.filter(name__endswith='M')
    data = Product.objects.filter(tags__isnull=True)

    context = {
        'data' : data
    }
    return render(request,'product/debug.html',context)


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(Product=self.get_object())
        context["related_items"] = Product.objects.filter(brand=self.get_object().brand)
        return context


class BrandList(ListView):
    model = Brand


class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.get(slug = self.kwargs['slug'])
        return context

    
