from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import Product, Brand

class ProductListSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    count_reviews = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_avg_rate(self, product):
        avg = product.product_review.aggregate(rate_avg=Avg('rate'))
        return  avg['rate_avg'] if avg['rate_avg'] else 0

    def get_count_reviews(self, product):
        count_reviews = product.product_review.all().count()
        return count_reviews
    

class ProductDetailsSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'