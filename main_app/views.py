from django.shortcuts import render, redirect
from .forms import CleanedForm
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
    cleaned_form = CleanedForm()
    return render(request, 'sneakers/detail.html', {
        'sneaker': sneaker, 'cleaned_form': cleaned_form
    })


def add_cleaned(request, sneaker_id):
    form = CleanedForm(request.POST)
    if form.is_valid():
        new_cleaned = form.save(commit=False)
        new_cleaned.sneaker_id = sneaker_id
        new_cleaned.save()
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


