from django.urls import path
from .views import ListOrder, checkout, add_to_cart
urlpatterns = [
    path('', ListOrder.as_view(), name='order_list'),
    path('checkout', checkout, name='checkout'),
    path('add-to-cart', add_to_cart, name='add_to_cart')
]
