from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    photo_profile = models.ImageField(upload_to="photos de profile" ,default="profile\icon_profile.png")
    numero_telephone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField()
    rue = models.CharField(blank=True,max_length=255)
    ville = models.CharField(blank=True,max_length=100)
    code_postal = models.CharField(blank=True,max_length=20)
    pays = models.CharField(blank=True,max_length=100)
    
    def save(self, *args, **kwargs):
        self.address = f"{self.rue}, {self.ville}, {self.pays}" if self.rue or self.ville or self.pays else ''
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username
