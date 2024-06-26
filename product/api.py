from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductListSerializer, ProductDetailsSerializer, BrandListSerializer, BrandDetailsSerializer
from .models import Product, Brand
from .filter_by_price_name import ProductFilter
from .custom_pagination import CustomPagination


# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:20] # list
#     data = ProductSerializer(products, context={'request':request}, many=True).data 
        # take list  ----> json , many = True so return many
#     return Response({'products':data})


# @api_view(['GET'])
# def product_detail_api(request, pk):
#     product = Product.objects.get(id=pk) 
#     data = ProductSerializer(product, context={'request':request}).data
#     return Response({'product':data})




class PeoductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtittle', 'description']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter

class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    permission_classes = [IsAuthenticated]


class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    pagination_class = CustomPagination


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailsSerializer