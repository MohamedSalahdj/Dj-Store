from rest_framework import serializers
from django.db.models.aggregates import Avg
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Product, Brand, Review

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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductDetailsSerializer(TaggitSerializer, serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    avg_rate = serializers.SerializerMethodField()
    reviews = ReviewSerializer(source='product_review', many=True)
    count_reviews = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self, product):
        avg = product.product_review.aggregate(rate_avg=Avg('rate'))
        return avg['rate_avg'] if avg['rate_avg'] else 0
    
    def get_count_reviews(slef, product):
        count_reviews = product.product_review.all().count()
        return count_reviews

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailsSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='brand_product', many=True)
    class Meta:
        model = Brand
        fields = '__all__'