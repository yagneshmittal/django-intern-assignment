from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def test_task():
    print("Starting background task...")
    time.sleep(5)
    print("Task finished!")
    return "done"

@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to the Django Internship App!"
    message = "Thank you for registering. We're glad to have you on board."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print(f"✅ Sent welcome email to {user_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {user_email}. Error: {e}")
