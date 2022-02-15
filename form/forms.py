from ast import Mod
import imp
from django.forms import ModelForm
from .models import Response

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['name', 'email', 'phone', 'address']