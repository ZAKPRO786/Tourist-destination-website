
from .models import TouristDestination
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class DestinationForm(forms.ModelForm):
    class Meta:
        model = TouristDestination
        fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'image', 'description']
        widgets = {
            'place_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter place name'}),
            'weather': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter weather details'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter district'}),
            'google_map_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Google Map URL'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
