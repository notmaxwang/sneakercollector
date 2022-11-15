from django.shortcuts import render
from .models import Sneaker


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneakers_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {
        'sneakers': sneakers
    })

def sneakers_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    return render(request, 'sneakers/detail.html', {'sneaker': sneaker})