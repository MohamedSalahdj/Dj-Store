from django.urls import path
from .views import ListOrder, checkout
urlpatterns = [
    path('', ListOrder.as_view(), name='order_list'),
    path('checkout', checkout, name='checkout')
]
