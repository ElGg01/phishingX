from django.db import models


# Create your models here.
class Victim(models.Model):
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.email
