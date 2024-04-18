from django.urls import path
from .views import ListOrder
urlpatterns = [
    path('', ListOrder.as_view(), name='order_list'),
]
