from django.db import models

# Create your models here.

class Profile(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.CharField(max_length=100)
        summary = models.TextField()
        profile_image = models.ImageField(upload_to='images/')

class Skill(models.Model):
        name = models.CharField(max_length=100)
        category = models.CharField(max_length=100)

class Contactmessage(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.TextField()
        sent_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return f"Message from {self.name} ({self.email})"