from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, queryset_debug
from .api import PeoductListApi, ProductDetailApi, BrandListApi, BrandDetailApi

urlpatterns = [
    path('',ProductList.as_view(), name='product_list'),
    path('debug',queryset_debug),
    path('<slug:slug>',ProductDetail.as_view(), name='product_detail'),
    path('brand/', BrandList.as_view(), name='brand_list'),
    path('brand/<slug:slug>/', BrandDetail.as_view(), name='brand_details'),

    #api urls
    path('api/list', PeoductListApi.as_view()),
    path('api/productdetail/<int:pk>', ProductDetailApi.as_view()),
    path('api/brand/list/', BrandListApi.as_view()),
    path('api/brand/<int:pk>/', BrandDetailApi.as_view()),

]
