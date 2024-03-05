from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.Restaurants.as_view(), name='all-restaurants'),
    path('restaurants/<uuid:restaurant_id>/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    path('recipes/', views.AllRecipes.as_view(), name='all-recipes'),
    path('ingredients/', views.AllIngredients.as_view(), name='all-ingredients'),
    path('ingredients/<uuid:ingredient_id>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
    path('api/recipes/', views.Recipes.as_view(), name='recipes-api'),
    path('api/recipes/<uuid:recipe_id>/', views.RecipeDetail.as_view(), name='recipe-detail-api'),
    path('api/ingredients/', views.Ingredients.as_view(), name='ingredients-api'),
    path('api/ingredients/<uuid:ingredient_id>/', views.IngredientDetail.as_view(), name='ingredient-detail-api'),
    path('restaurants/by_recipe/<str:recipe_name>/', views.RestaurantsByRecipe.as_view(), name='restaurants-by-recipe'),
    path('restaurants/<uuid:restaurant_id>/recipes/', views.RestaurantRecipes.as_view(), name='restaurant-recipes'),
    path('ingredients/<uuid:ingredient_id>/recipes/', views.IngredientRecipes.as_view(), name='ingredient-recipes'),
    path('restaurants/<uuid:restaurant_id>/ingredients/', views.RestaurantIngredients.as_view(), name='restaurant-ingredients'),
    path('recipes/<uuid:recipe_id>/ingredients/', views.RecipeIngredients.as_view(), name='recipe_ingredients'),
]
