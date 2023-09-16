from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=75)
    logo = models.ImageField(_('Logo'), upload_to='company')
    subtitle = models.TextField(_('SubTitle'), max_length=300)
    fb_link = models.URLField(_('Facebook'), null=True, blank=True)
    tw_link = models.URLField(_('Twitter'), null=True, blank=True)
    yt_link = models.URLField(_('Youtube'), null=True, blank=True)
    phone = models.TextField(_('Phone'), max_length=45, null=True, blank=True)
    email = models.TextField(_('Email'), max_length=45, null=True, blank=True)
    address = models.TextField(_('Address'), max_length=150, null=True, blank=True)
    ios_app = models.TextField(_('IOS'), max_length=150, null=True, blank=True)
    android_app = models.TextField(_('Android'), max_length=150, null=True, blank=True)
    call_us = models.TextField(_('Call US'), max_length=150, null=True, blank=True)
    email_us = models.TextField(_('Email US'), max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name