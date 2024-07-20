from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Order, OrderDetail, Cart, CartDetail, Coupon 
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
            cart_detail, created = CartDetail.objects.get_or_create(cart=cart, product=product)
            cart_detail.quantity = int(quantity)
            cart_detail.total = round(product.price * cart_detail.quantity ,2)
            cart_detail.save()
            
            messages.success(request, "Added to cart successfully")
    else:
        messages.error(request, "Enter the right quantity")

    return redirect(f'/products/{product.slug}')


@login_required
def increase_quantity(request):
    product = get_object_or_404(Product, id=request.POST['product_id'])
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_detail = CartDetail.objects.get(cart=cart, product=product)
    if cart_detail.quantity < product.quantity:
        cart_detail.quantity +=1
        cart_detail.total = round( product.price * cart_detail.quantity, 2)
        cart_detail.save()
        messages.success(request, "increase quantity")
    else:
        messages.error(request, "quantity lower than it")
    return redirect('/')

@login_required
def decrease_quantity(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_detail = CartDetail.objects.get(cart=cart, product=product)
    if cart_detail.quantity > 1:
        cart_detail.quantity -=1
        cart_detail.total = round( product.price * cart_detail.quantity, 2)
        cart_detail.save()
        messages.success(request, "decrease quantity")
    else:
        messages.error(request, "quantity lower than it")
    return redirect('/')


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


