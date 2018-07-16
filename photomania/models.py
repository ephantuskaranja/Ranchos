from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.location
        class Meta:
            ordering = ['location']



class Category(models.Model):
    category = models.CharField(max_length = 50)

    def __str__(self):
        return self.category
        class Meta:
            ordering = ['category']


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =50)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    @classmethod
    def get_images(cls):
       images = cls.objects.all()
       return images

    def __str__(self):
        return self.name
        class Meta:
            ordering = ['name']

    def save_image(self):
        self.save()

    @classmethod
    def searched_categories(cls, category):
        category = cls.objects.filter(description__icontains=category)
        return category
