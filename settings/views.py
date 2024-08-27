from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Company
from product.models import Product, Brand, Review
from django.db.models.aggregates import Count


@cache_page(60 * 15)
def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('brand_product'))
    sale_products = Product.objects.filter(flag='Sale')[:10]
    feature_products = Product.objects.filter(flag='Feature')[:6]
    new_products = Product.objects.filter(flag='New')[:8]
    revviews = Review.objects.all()[:10]
    
    context = {
        'brands': brands,
        'sale_products': sale_products,
        'feature_products': feature_products,
        'new_products': new_products,
        'revviews': revviews,
    }
    
    return render(request, 'settings/home.html',context)
