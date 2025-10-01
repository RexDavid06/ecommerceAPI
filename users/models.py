from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    GENDER = (
        ("male", "Male"),
        ("female", "Female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150, null=True, blank=True)
    lastname = models.CharField(max_length=150, null=True, blank=True)
    nationality = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)

    def __str__(self):
        return str(self.user)
    
    
