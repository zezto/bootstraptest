from django.http import HttpResponse
from .models import Image
from django.shortcuts import render
def index(request):
    return render(request, 'website/index.html')

def details(request):
    image = Image.objects.all()
    context = {'image': image}
    return render(request, 'website/bamboozled.html', context)

def about(request):
    return render(request, 'website/about.html')

def terms(request):
    return render(request,'website/terms.html')