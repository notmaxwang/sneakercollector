from django.shortcuts import render

sneakers = [
    {'name': 'Jordan 1', 'colorway': 'Bred', 'retail_price': '$190'},
    {'name': 'Jordan 3', 'colorway': 'Black Cement', 'retail_price': '$220'},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneakers_index(request):
    return render(request, 'sneakers/index.html', {
        'sneakers': sneakers
    })