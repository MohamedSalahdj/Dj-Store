from django.urls import path
from .views import register, profile, activate_accounts

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/<str:username>/', profile, name='profile'),
    path('activate/<str:username>/', activate_accounts, name='activate_account'),
]
