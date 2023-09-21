from django.db import models

# Create your models here.

class URL(models.Model):
    link = models.URLField(max_length=1000)
    shortened = models.CharField(max_length=5)