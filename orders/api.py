from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from product.models import Product
from .models import Cart, CartDetail
from .serializers import CartDetailSerializer, CartSerializer


class CartCreatRetriveDeleteAPI(generics.GenericAPIView): 
    
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})
        

    def post(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        item = CartDetail.objects.get(id=request.data['item_id'])
        item.delete()

        cart = Cart.objects.get(user=user, status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'msg':'Deleted item succsssfully', 'cart':data})