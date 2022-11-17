from django.shortcuts import render, redirect
from .forms import ShoelaceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    shoelace_form = ShoelaceForm()
    return render(request, 'sneakers/detail.html', {
        'sneaker': sneaker, 'shoelace_form': shoelace_form
    })


def add_shoelace(request, sneaker_id):
    form = ShoelaceForm(request.POST)
    if form.is_valid():
        new_shoelace = form.save(commit=False)
        new_shoelace.sneaker_id = sneaker_id
        new_shoelace.save()
    return redirect('detail', sneaker_id = sneaker_id)


class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'
    success_url = '/sneakers'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['name', 'colorway', 'retail_price']


class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers'


