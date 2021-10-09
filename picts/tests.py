from django.test import TestCase

# Create your tests here.
from .models import Category,Location,Image
import datetime as dt

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(name='Kenya')
        self.name = Location(name='Kenya')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location))
        
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Car')
        self.name = Category(name='Car')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))
    
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save()

        self.category = Category(name='home')
        self.category.save()

        self.image_test = Image(id=1, image='image.jpg', description='this is a test image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)


    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


