from django.forms import ModelForm
from .models import Shoelace

class ShoelaceForm(ModelForm):
    class Meta:
        model = Shoelace
        fields = ['date', 'color']