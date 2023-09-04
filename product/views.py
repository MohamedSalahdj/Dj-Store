from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Product_Images, Brand, Review

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'


