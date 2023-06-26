from django.views.generic import DetailView, UpdateView, CreateView, ListView
from . import models

# Create your views here.
class RecipeList(ListView):
    model = models.Recipe

class RecipeDetail(DetailView):
    model = models.Recipe

class RecipeCreate(CreateView):
    model = models.Recipe

class RecipeUpdate(UpdateView):
    model = models.Recipe
