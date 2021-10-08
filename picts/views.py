from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from .models import Image, Location,categories

# Create your views here.

def home(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = categories.objects.all()

    if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)

    elif 'category' in request.GET and request.GET['category']:
        cat = request.GET.get('categories')
        images = Image.view_category(cat)
        return render(request, 'all-images.html', {"name":name,"images":images,"cat":cat })

    return render(request,"all-images.html",{"images":images,"location":location,"category":category})

def search_results(request):

    if 'categories' in request.GET and request.GET['categories']:
        search_images = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request,"image.html", {"image":image})