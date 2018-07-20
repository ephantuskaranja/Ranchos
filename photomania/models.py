from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.location
        class Meta:
            ordering = ['location']

    def save_location(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length = 50)

    def __str__(self):
        return self.category

        class Meta:
            ordering = ['category']

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()




class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    name = models.CharField(max_length =50)
    description = models.TextField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Location,  null=True, blank=True)
    category = models.ForeignKey(Category,  null=True, blank=True)

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

    def delete_image(self):
        self.delete()


    @classmethod
    def searched_categories(cls, category):
        category = cls.objects.filter(description__icontains=category)
        return category
