from django.db import models

# Create your models here.
class Page(models.Model):
    url_path = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField() 