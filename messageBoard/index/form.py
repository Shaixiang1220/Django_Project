from django import forms
from .models import *

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
