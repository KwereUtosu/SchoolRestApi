from django.db import models

# Create your models here.

class School(models.Model):
    term_name = models.CharField(max_length=30)
    name = models.CharField(max_length=200)