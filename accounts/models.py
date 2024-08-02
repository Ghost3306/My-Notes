from django.db import models
from django.contrib.auth.models import User
from Base.models import BaseModel
from Base.send_email import send_pin_email
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    def __str__(self) ->str:
        return self.user.username
    

@receiver(post_save, sender=User)
def account_create_instance(sender,instance,created, **kwargs):
    try:
        Profile.objects.create(user=instance)
        email = instance.email
        user = instance.user
        send_pin_email(email,user)

    except Exception as e:
        print(e)
