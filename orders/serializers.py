from rest_framework import serializers
from .models import Cart, CartDetail, Order, OrderDetail


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'
