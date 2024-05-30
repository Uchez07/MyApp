from django import forms
from django.forms import ModelForm
from .models import Room  # Import your Room model here
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room  # Specify the model here
        fields = '__all__'  # You can specify specific fields if needed
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

