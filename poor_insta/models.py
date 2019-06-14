from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Photo(models.Model):
    path = models.CharField(max_length=512)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


