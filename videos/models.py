from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Video(models.Model):

    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Gaming', 'Gaming'),
        ('Lectures', 'Lectures'),
        ('Sports', 'Sports'),
        ('Other', 'Other'),
    ]

    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='videos')
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='Other')
    views = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title