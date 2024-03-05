from django.db import models
import uuid


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=False, verbose_name="Name")

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Name")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    recipes = models.ManyToManyField(Recipe, related_name='ingredients')

    def __str__(self):
        return self.name
