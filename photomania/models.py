from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 50)
    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length = 50)
    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =50)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
