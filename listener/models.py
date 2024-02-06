from django.db import models

# Create your models here.
class Posts(models.Model):
    postContent = models.CharField(max_length=1000)