from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime
from product.models import Product
from .models import Cart, CartDetail, Order, OrderDetail, Coupon
from .serializers import CartSerializer, OrderSerializer, OrderDetailSerializer


class ListOrderAPI(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self): 
        queryset = Order.objects.filter(user=User.objects.get(username=self.kwargs['username']))
        return queryset

    # def list(self, request, *args, **kwargs):
    #     queryset =  super(ListOrderAPI, self).get_queryset()
    #     user = User.objects.get(username=self.kwargs['username'])
    #     queryset = queryset.filter(user=user)
    #     data = OrderSerializer(queryset, many=True).data    
    #     return Response({'orders':data})

class OdrerDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()


class CartCreatRetriveDeleteAPI(generics.GenericAPIView): 
    
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})
        

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.data['product_id'])
        quantity = request.data['quantity']

        cart = Cart.objects.get(user=user)
        cartdetail, created = CartDetail.objects.get_or_create(cart=cart, product=product)
        cartdetail.quantity =int(quantity)
        cartdetail.total = round(product.price * cartdetail.quantity, 2)
        cartdetail.save()

        data = CartSerializer(cart).data  
        return Response({'msg':"Added item successfully", 'cart':data})


    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        item = CartDetail.objects.get(id=request.data['item_id'])
        item.delete()

        cart = Cart.objects.get(user=user, status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'msg':'Deleted item succsssfully', 'cart':data})
    


class ApplyCouponAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=User.objects.get(username=self.kwargs['username']), status='Inprogress')

        coupon = get_object_or_404(Coupon, code=self.request.data['coupon_code'])

        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()    
            if today_date >= coupon.start_date.date() and today_date <= coupon.end_date.date():
                coupon_value = cart.cart_total * (coupon.discount /100)
                cart_total = cart.cart_total - coupon_value

                cart.coupon = coupon
                cart.total_with_coupon = cart_total
                cart.save()
                data = CartSerializer(cart).data
                return Response({'msg':"Coupon appllied successfully", 'cart' : data})
            else:
                return Response({'msg':"Coupon date expired"})
        else:
            return Response({'msg':'No coupon found'})
        

class CreateOrderAPI(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user, status='Inprogress')
        cart_detail = CartDetail.objects.filter(cart=cart)

        new_order = Order.objects.create(
            user = user,
            coupon = cart.coupon,
            total_with_coupon = cart.total_with_coupon
        )

        for item in cart_detail:
            OrderDetail.objects.create (
                order = new_order,
                product = item.product,
                quantity =  item.quantity,
                price = item.product.price,
                total = round(item.product.price * int(item.quantity), 2)
            )

        cart.status = 'Completed'
        cart.save()

        return Response({'msg':"Created order successfully"})