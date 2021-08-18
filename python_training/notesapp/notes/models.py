from django.db import models
class Notes(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
# Create your models here.
