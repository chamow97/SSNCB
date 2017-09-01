from django.db import models

class contests(models.Model):
    contest_name = models.CharField(max_length=300)
    date = models.DateField
    type = models.IntegerField
    time = models.DateTimeField
    is_rated = models.BooleanField

class practice(models.Model):
    name = models.CharField(max_length=300)
    type = models.IntegerField
    