from django.forms import ModelForm
from .models import *

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre','precio','descuento','precio_final','categoria','imagen']