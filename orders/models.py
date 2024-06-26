from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from product.models import Product
from utils.generate_caode import generate_code


cart_status = (
    ('Inprogress', 'Inprogress'),
    ('Completed', 'Completed')
)

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.CASCADE)
    status = models.CharField(choices=cart_status, max_length=10)
    coupon = models.ForeignKey('Coupon', related_name='cart_coupon', on_delete = models.SET_NULL, null=True, blank=True)
    total_with_coupon = models.FloatField(null=True, blank=True)


    def __str__(self):
        return str(self.user)
    
    @property
    def cart_total(self):
        total = 0
        for item in self.cart_detail.all():
            total += item.total
        return round(total, 2)


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_detail_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.cart)


order_status = (
    ('Received', 'Received'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.CASCADE)
    code = models.CharField(default=generate_code(), max_length=8, unique=True)
    status = models.CharField(choices=order_status, max_length=10, default='Received')
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete = models.SET_NULL, null=True, blank=True)
    total_with_coupon = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.user)




class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_detail_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()


    def __str__(self):
        return str(self.order)


class Coupon(models.Model):
    code = models.CharField(max_length=25)
    discount = models.FloatField()
    quantity = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs): 
        self.end_date = self.start_date + timedelta(weeks=7)
        super(Coupon, self).save(*args, **kwargs)

    