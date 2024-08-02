from django.conf import settings
from django.core.mail import send_mail
import random

def send_pin_email(email,user):
    subject = "Your account Pin"
    email_from = settings.EMAIL_HOST_USER
    pin = random.randint(0000,9999)
    message =f"""
Dear {user},

As you create account on My Notes, please find your account pin below:

Pin: {pin}

We highly recommend that you take the following security precautions:


1. Do not share your password with anyone and avoid using the same password for multiple accounts.

If you have any questions or need further assistance, please feel free to reach out to us.

Thank you for your attention to this matter.

Best regards,
My Notes
"""
    send_mail(subject,message,email_from,[email])