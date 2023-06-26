from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path("all/", views.RecipeList.as_view(), name="list"),
    path("<int:pk>/", views.RecipeDetail.as_view(), name="detail"),
    path("create/", views.RecipeCreate.as_view(), name="create"),
    path("<int:pk>/update/", views.RecipeUpdate.as_view(), name="update"),
]