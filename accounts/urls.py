from django.urls import path
from .views import register, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
