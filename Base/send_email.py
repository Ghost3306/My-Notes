from django.conf import settings
from django.core.mail import send_mail
import random

def send_pin_email(email,email_token):
    try:    
        subject = "Your account Pin"
        email_from = settings.EMAIL_HOST_USER
        
        message =f"""
    Dear {email},

    As you create account on My Notes, please find your account pin below:

    Link : http://127.0.0.1:8000/accounts/activate/{email_token}/

    We highly recommend that you take the following security precautions:


    1. Do not share your password with anyone and avoid using the same password for multiple accounts.

    If you have any questions or need further assistance, please feel free to reach out to us.

    Thank you for your attention to this matter.

    Best regards,
    My Notes
    """
        print('sending email')
        send_mail(subject,message,email_from,[email])
        print('email sent')
    except Exception as e:
        print(e)