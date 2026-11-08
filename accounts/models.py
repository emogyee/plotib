from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    channel_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)                    
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.user.username},({self.channel_name})'s Profile'"