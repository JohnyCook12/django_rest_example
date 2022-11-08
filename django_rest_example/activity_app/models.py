from django.db import models

# Create your models here.
class Activity(models.Model):
    info = models.CharField(max_length=200)
    # user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    # user = models.CharField(max_length=200, default='nobody')
    when = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE)
