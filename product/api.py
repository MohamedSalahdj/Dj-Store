from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer, BrandSerializer
from .models import Product, Brand


# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:20] # list
#     data = ProductSerializer(products, context={'request':request}, many=True).data #json
#     return Response({'products':data})


# @api_view(['GET'])
# def product_detail_api(request, pk):
#     product = Product.objects.get(id=pk) 
#     data = ProductSerializer(product, context={'request':request}).data
#     return Response({'product':data})


class PeoductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer