from django.db import models
from django.conf import settings

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=64, blank=True)
    location_type = models.PositiveSmallIntegerField()
    location = models.TextField(blank=True)
    instructions = models.TextField()
    # instructions_file = models.FileField()
    servings = models.CharField(max_length=32, blank=True)
    prep_time = models.CharField(max_length=32, blank=True)
    cook_time = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=128, blank=True)
    # TODO: tags (many to many)
    personal_notes = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    # TODO: shared users

# TODO: ingredients