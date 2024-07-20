from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from utils.generate_caode import generate_code


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(_('User Image'), upload_to='accounts', null=True, blank=True)
    code =  models.CharField(_('User Code Verify'), max_length=6, default=generate_code(6))

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create (
            user = instance
        )


PHONE_TYPE = (
    ('Primary','Primary'),
    ('Secondary','Secondary')
)

class ContactNumber(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, related_name='user_number')
    type = models.CharField(_('Mobile Type'), choices=PHONE_TYPE, max_length=9)
    phone = models.CharField(_('Mobile Phone'), max_length=13)

    def __str__(self):
        return self.user.username


ADDRESS_TYPE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussines', 'Bussines'),
    ('Other' , 'Other')
)

class Address(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, related_name='user_address')
    type = models.CharField(_('Address Type'), choices=ADDRESS_TYPE, max_length=8)
    Address = models.TextField(_('User Address'), max_length=150)

    def __str__(self):
        return self.user.username    

