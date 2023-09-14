from django import forms 
from url.models import URL

class UrlForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['link']