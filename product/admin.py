from django.contrib import admin
from .models import Product, Product_Images, Brand, Review


class ProductImagesAdmin(admin.TabularInline):
    model = Product_Images


class CustomiseProduct(admin.ModelAdmin):
    list_display = ['name', 'flag', 'price', 'brand']
    list_filter = ['price', 'flag']
    search_fields = ['name', 'brand', 'subtittle']
    inlines = [ProductImagesAdmin,]


admin.site.register(Product, CustomiseProduct)
admin.site.register(Product_Images)
admin.site.register(Brand)
admin.site.register(Review)