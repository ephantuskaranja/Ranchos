from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
from django.db.models import Q

# Create your views here.
def welcome(request):
    images = Image.get_images()
    return render(request, 'photomania/home.html',{"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_categories = Image.searched_categories(category)
        message = f"{category}"

        return render(request, 'photomania/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photomania/search.html',{"message":message})
