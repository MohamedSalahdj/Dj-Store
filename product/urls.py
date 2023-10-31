from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, queryset_debug
from .api import PeoductListApi, ProductDetailApi

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',queryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    path('brand/', BrandList.as_view()),
    path('brand/<slug:slug>/', BrandDetail.as_view()),

    #api urls
    path('api/list', PeoductListApi.as_view()),
    path('api/productdetail/<int:pk>', ProductDetailApi.as_view())
]
