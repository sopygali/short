from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Logins(models.Model): #rename Link
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    link = models.URLField()

