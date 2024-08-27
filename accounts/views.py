from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail

from .forms import UserRegistrationForm, UserActivateForm
from .models import Profile, ContactNumber, Address
from utils.send_email import send_emails

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # get username using cleaned_data 
            username = form.cleaned_data['username']
            # get email using get method 
            email = request.POST.get('email')

            # Save new user but don't activate yet
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.save()
            profile = Profile.objects.get(user__username=username)
            
            # Send activation email
            
            send_emails(username, profile.code, email)

            return redirect(reverse("activate_account", args=[username]))

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def activate_accounts(request, username):

    form = UserActivateForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            code = form.cleaned_data['code']
            profile = Profile.objects.get(user__username=username)
            if code == profile.code:
                profile.code = ''
                user = User.objects.get(username=username)
                user.is_active = True
                user.save()
                profile.save()
                return redirect("login")
    else:
        form = UserActivateForm()

    context = {
        "form": form
    }

    return render(request, "accounts/activate.html", context)


def profile(request, username):
    user = User.objects.select_related(
        'user_profile'
    ).prefetch_related(
        'user_number', 'user_address'
    ).get(username=username)
    
    context = {
        'user': user
    }

    return render(request, 'accounts/profile.html', context)  