from celery import shared_task
import time
from django.core.mail import send_mail

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
    from_email = "yagneshmittal3010@example.com"
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
    print(f"Sent welcome email to {user_email}")
