from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class TestImage(TestCase):
    
    # set up method
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

        self.category = Category(name='home')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location,
                                category=self.category)
        
     
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))
        
        # testing save method
    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)