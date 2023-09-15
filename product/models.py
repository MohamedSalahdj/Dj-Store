from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.aggregates import Avg

flags_type = (
    ('Sale', 'Sale'),
    ('New', 'New'),
    ('Feature', 'Feature'),
)
class Product(models.Model):
    name = models.CharField(_('Name'), max_length=125)
    image = models.ImageField(_('Image'), upload_to='products')
    price = models.FloatField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))
    flag = models.CharField(_('Flag'), max_length=7, choices=flags_type)
    description = models.TextField(_('Description'), max_length= 7000)
    sku = models.CharField(_('SKU'), max_length=12)
    subtittle = models.CharField(_('Subtitle'), max_length=300)
    brand = models.ForeignKey('Brand', verbose_name=_('Brand'), related_name='brand_product',on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def avg_rate(self):
        avg = self.product_review.aggregate(product_avg=Avg('rate'))
        return avg['product_avg']  if avg['product_avg'] else 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)




class Product_Images(models.Model):
    image = models.ImageField(_('Image'), upload_to='products-images')
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='product_images', on_delete=models.CASCADE)



class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=70)
    image = models.ImageField(_('Image'), upload_to='brands')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)


class Review(models.Model):
    review = models.CharField(_('Review'), max_length= 255)
    rate = models.IntegerField(_('Rate'))
    created_at = models.DateTimeField(_('Created at'), default=timezone.now)
    customer = models.ForeignKey(User, verbose_name=_('Customer'), related_name='customer_review', on_delete=models.SET_NULL, null=True)
    Product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='product_review', on_delete=models.CASCADE)

    def __str__(self):
        return '- '+ str(self.customer) + ' # ' +self.review 