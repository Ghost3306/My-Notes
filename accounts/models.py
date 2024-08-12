from django.db import models
from django.contrib.auth.models import User
from Base.models import BaseModel
from Base.send_email import send_pin_email
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100)

    def __str__(self) ->str:
        return self.user.username
    

@receiver(post_save, sender=User)
def account_create_instance(sender,instance,created, **kwargs):
    try:
        email_token = str(uuid.uuid4())
        Profile.objects.create(user=instance,email_token=email_token)
        email = instance.email
        print('form model',instance.email)
        send_pin_email(email,email_token)

    except Exception as e:
        print(e)
