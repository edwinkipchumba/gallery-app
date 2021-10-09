from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default='')



    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image
        
    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
        
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    @classmethod
    def filter_by_location(cls, location):
        img_location = Image.objects.filter(location__name=location).all()
        return img_location

    class Meta:
        ordering = ['date']
    