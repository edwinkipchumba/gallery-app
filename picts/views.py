from django.shortcuts import render
from .models import Image, Location

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'pictures/index.html', {'images': images[::-1], 'locations': locations})