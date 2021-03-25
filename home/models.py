from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=14, default='')
    content = models.TextField(max_length=500, default='')

    def __str__(self):
        return 'Message From: ' + self.name
