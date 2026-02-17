from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # mobile_number = models.CharField(max_length=15, blank=True, null=True)
    # hobby = models.CharField(max_length=100, blank=True, null=True)
    # country = models.CharField(max_length=50, blank=True, null=True)
    # profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    # def __str__(self):
    #     return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    hobby = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
