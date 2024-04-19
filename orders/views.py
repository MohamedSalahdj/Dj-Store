from django.shortcuts import render
from django.views.generic import ListView
from .models import Order, OrderDetail, Cart, CartDetail, Cupon 


class ListOrder(ListView):
    model = Order
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset




def checkout(request):
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'cart_detail' : cart_detail
    }

    return render(request, 'orders/checkout.html', context)
