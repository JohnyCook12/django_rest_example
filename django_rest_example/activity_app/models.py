from django.db import models

# Create your models here.
class Activity(models.Model):
    info = models.CharField(max_length=200)
    user = models.CharField(max_length=200, default='nobody')
    when = models.DateTimeField(auto_now_add=True)
