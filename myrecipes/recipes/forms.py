from django.forms import forms

from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        exclude = ("owner",)