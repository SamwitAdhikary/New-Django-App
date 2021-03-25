from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='')
    slug = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=50, default='Samwit Adhikary')
    content = models.TextField()
    short_desc = models.CharField(max_length=219, default='')
    timestamp = models.DateTimeField()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
