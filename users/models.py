from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

import os


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, default="", unique=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    @receiver(post_save,  sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, related_name="Teacher",  on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(
        User, related_name="Student",  on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Admin(models.Model):
    user = models.OneToOneField(
        User, related_name="Admin",  on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
