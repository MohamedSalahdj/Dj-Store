from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q, F, Value 
from django.db.models.aggregates import Min, Max, Sum, Count, Avg 
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
    # data = Product.objects.filter(tags__isnull=True)

    #filter with time 
    # data = Review.objects.filter(created_at__year=2023)
    # data = Review.objects.filter(created_at__month=2025)

    #filter 2 values 
    # data = Product.objects.filter(price__lt=1000, quantity__lt=15) #and
    # data = Product.objects.filter(Q(price__lt=2000) & Q(quantity__gt=10)) # and
    # data = Product.objects.filter( Q(price__lt=1000) | Q(quantity__gt=5) ) # OR
    # data = Product.objects.filter(Q(price__gt=1000) & ~Q(quantity__lt=15)) # and with not
    
    #check two value equal  
    # data = Product.objects.filter(price=F('quantity'))


    #Ordering One value
    # data = Product.objects.all().order_by('name') #= Product.objects.order_by('name') ASC
    # data = Product.objects.order_by('-name') #DESC
    # data = Product.objects.order_by('name').reverse() #DESC
    
    # ordering with tow value
    # data = Product.objects.order_by('name', '-quantity')

    #retrive some value 
    # data = Product.objects.order_by('name')[0]
    # data = Product.objects.earliest('name')
    # data = Product.objects.latest('name')

    #slice 
    # data = Product.objects.all()[:10]

    #select Columns
    # data = Product.objects.values('name', 'price') #dict
    # data = Product.objects.values('name', 'price', 'flag', 'quantity', 'brand__name') #dict
    # data = Product.objects.values_list('name', 'price', 'flag', 'quantity', 'brand__name') #tuple

    #remove dublicate
    # data = Product.objects.all().distinct()

    #only , defer
    # data = Product.objects.only('name','price','flag')
    # data = Product.objects.defer('flag')

    # Aggergations
    # data = Product.objects.aggregate(Sum('quantity'))
    # data = Product.objects.aggregate(Avg('price'))

    #annotate 
    # data = Product.objects.annotate(is_new=Value(True))
    data = Product.objects.annotate(price_with_discount=F('price')*0.959)


    context = {
        'data' : data
    }
    return render(request,'product/debug.html',context)


class ProductList(ListView):
    model = Product
    paginate_by = 28
    


class ProductDetail(DetailView):
    model = Product   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(Product=self.get_object())
        context["related_items"] = Product.objects.filter(brand=self.get_object().brand)
        return context


class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.annotate(product_count=Count('brand_product'))
    paginate_by = 20


class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('brand_product'))[0]
        return context

    
