from django.contrib import admin
from .models import Profile, Address, ContactNumber

admin.site.register(Profile)
admin.site.register(ContactNumber)
admin.site.register(Address)