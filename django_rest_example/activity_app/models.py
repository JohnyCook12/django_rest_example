from django.db import models

# Create your models here.
class Activity(models.Model):
    info = models.CharField(max_length=200)
    when = models.DateTimeField('when happened')