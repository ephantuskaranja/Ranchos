from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =50)
    description = models.TextField()


class Location(models.Model):
    location = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ForeignKey(Image)


class Category(models.Model):
    category = models.CharField(max_length = 50)
    image = models.ForeignKey(Image)
