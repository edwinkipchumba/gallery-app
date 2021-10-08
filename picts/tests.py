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
        
        # test delete method
    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
        # test update method
    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)