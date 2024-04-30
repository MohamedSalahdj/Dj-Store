from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Order, OrderDetail, Cart, CartDetail, Coupon 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from product.models import Product

class ListOrder(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

@login_required
def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']
    if quantity.isnumeric() and int(quantity) <= product.quantity:
        cart = Cart.objects.get(user=request.user, status='Inprogress')
        cart_details, created = CartDetail.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_details.quantity += int(quantity)
            cart_details.total = round(product.price * cart_details.quantity, 2)
            print(cart_details.quantity)
            cart_details.save()
        else:
            cart_details.quantity = int(quantity)
            cart_details.total = round(product.price * cart_details.quantity, 2)
            cart_details.save()        
    return redirect(f'/products/{product.slug}')


@login_required
def remove_from_cart(request, id):
    cart_detail = CartDetail.objects.get(product=id)
    cart_detail.delete()
    return redirect('/')



@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    context = {
        'cart': cart,
        'cart_detail' : cart_detail
    }

    return render(request, 'orders/checkout.html', context)


