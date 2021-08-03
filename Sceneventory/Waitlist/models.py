from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(max_length=11, unique=True)
    traffic = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name