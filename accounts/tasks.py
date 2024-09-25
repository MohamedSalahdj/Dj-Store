from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task



@shared_task
def send_emails(username, code, email):
    activation_link = f"http://127.0.0.1:8000/accounts/activate/{username}/?code={code}"

    subject = 'Activate Your Account'
    message = f'Welcome {username},\nUse this code {code} to activate your account\nPlease click the link below to activate your account:\n{activation_link}.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, email_from, recipient_list)