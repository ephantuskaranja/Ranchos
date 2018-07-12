from django.db import models

# Create your models here.

class Image(models.Model):
    # image = models.ImageField(upload_to = 'images/' blank = True)
    name = models.CharField(max_length =50)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()


class Location(models.Model):
    location = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ForeignKey(Image)


class Category(models.Model):
    category = models.CharField(max_length = 50)
    image = models.ForeignKey(Image)

    
