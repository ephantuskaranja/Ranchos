from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image, Category, Location


class LocationTestClass(TestCase):

   # Set up method
    def setUp(self):
        self.location = Location(location = 'Nairobi')

    #testing instance
    def test_instance(self):
       self.assertTrue(isinstance(self.location, Location))

    #testing save location method
    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    # setup method
    def setUp(self):
        self.category = Category(category = 'food')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    #testing save method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 1)

    #test delete method
    def test_delete_category(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.name = Image(name ='imagename')

    def test_instance(self):
        self.assertTrue(isinstance(self.name, Image))


    def test_save_image(self):
        self.name.save_image()
        image_name = Image.objects.filter(name='imagename')
        self.assertTrue(len(image_name)== 1)

    def test_delete_image(self):
        self.name.save_image()
        self.name.delete_image()
        image_name = Image.objects.all()
        self.assertTrue(len(image_name) == 0)
