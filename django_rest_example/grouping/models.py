from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    groups = models.ManyToManyField(Group, related_name='persons', blank=True)

    def __str__(self):
        return self.name