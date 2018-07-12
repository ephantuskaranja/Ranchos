from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.DecimalField(max_digits=9, decimal_places=6)



class Category(models.Model):
    category = models.CharField(max_length = 50)



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
