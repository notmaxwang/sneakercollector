from django.forms import ModelForm
from .models import Cleaned

class CleanedForm(ModelForm):
    class Meta:
        model = Cleaned
        fields = ['date', 'product']