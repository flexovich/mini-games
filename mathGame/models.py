from django.db import models

class Image(models.Model):
    image = models.CharField(max_length=50)
    result = models.IntegerField()
