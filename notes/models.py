from django.db import models
from Base.models import BaseModel
from accounts.models import Profile
# Create your models here.

class Notes(BaseModel):
    title = models.CharField(max_length=255)
    main = models.TextField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self) ->str:
        return self.title