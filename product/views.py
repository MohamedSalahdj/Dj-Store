from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Product_Images, Brand, Review


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product    
    context_object_name = 'product'

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

    
