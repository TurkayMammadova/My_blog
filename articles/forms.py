from django import forms
from .models import Articles

class AddarticlesForm(forms.ModelForm):
    class Meta:
        model=Articles
        fields=['title','content','article_image']
