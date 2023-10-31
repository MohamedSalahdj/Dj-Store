from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:20] # list
    data = ProductSerializer(products, context={'request':request}, many=True).data #json
    return Response({'products':data})


@api_view(['GET'])
def product_detail_api(request, pk):
    product = Product.objects.get(id=pk) 
    data = ProductSerializer(product, context={'request':request}).data
    return Response({'product':data})