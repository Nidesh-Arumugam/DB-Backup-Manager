from django.forms import ModelForm
from .models import databases

class DatabaseForm(ModelForm):
     class Meta:
       model = databases
       fields = '__all__'