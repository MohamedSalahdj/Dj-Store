from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, queryset_debug

urlpatterns = [
    path('',ProductList.as_view()),
    path('debug',queryset_debug),
    path('<slug:slug>',ProductDetail.as_view()),
    path('brand/', BrandList.as_view()),
    path('brand/<slug:slug>/', BrandDetail.as_view()),
]
