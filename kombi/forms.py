from django.forms import ModelForm
from kombi.models import Freighter

class RegisterForm(ModelForm):
    class Meta:
        model = Freighter
        fields = ['name','code','phone']
