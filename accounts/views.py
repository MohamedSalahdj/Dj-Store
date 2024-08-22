from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Profile, ContactNumber, Address


def register(request):
    pass



def profile(request):

    context = {
        
    }

    return render(request, 'registration/profile.html')