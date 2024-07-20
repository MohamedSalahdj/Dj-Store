from django.urls import path
from .views import ListOrder, checkout, add_to_cart, remove_from_cart, increase_quantity, decrease_quantity
from .api import CartCreatRetriveDeleteAPI, ListOrderAPI, OdrerDetailAPI, CreateOrderAPI, ApplyCouponAPI


urlpatterns = [
    path('', ListOrder.as_view(), name='order_list'),
    path('checkout', checkout, name='checkout'),
    path('add-to-cart', add_to_cart, name='add_to_cart'),
    path('increase-quantity/', increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:pk>', decrease_quantity, name='decrease_quantity'),
    path('<int:id>/remove-item', remove_from_cart, name='remove_from_cart'),


    #api-endpoint
    path('<str:username>/cart', CartCreatRetriveDeleteAPI.as_view()),
    path('<str:username>/list-order', ListOrderAPI.as_view()),
    path('<str:username>/<int:pk>/detail', OdrerDetailAPI.as_view()),
    path('<str:username>/create-order', CreateOrderAPI.as_view()),
    path('<str:username>/apply-coupon', ApplyCouponAPI.as_view()),

]
