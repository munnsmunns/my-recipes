from django.views.generic import DetailView, UpdateView, CreateView, ListView
from . import models, forms

# Create your views here.
class RecipeList(ListView):
    model = models.Recipe

class RecipeDetail(DetailView):
    model = models.Recipe

class RecipeCreate(CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm

class RecipeUpdate(UpdateView):
    model = models.Recipe
    form_class = forms.RecipeForm
