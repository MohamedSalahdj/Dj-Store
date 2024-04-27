from django.urls import path
from .views import ListOrder, checkout, add_to_cart, remove_from_cart
urlpatterns = [
    path('', ListOrder.as_view(), name='order_list'),
    path('checkout', checkout, name='checkout'),
    path('add-to-cart', add_to_cart, name='add_to_cart'),
    path('<int:id>/remove-item', remove_from_cart, name='remove_from_cart'),

]
