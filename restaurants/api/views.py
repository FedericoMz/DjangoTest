from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Restaurant, Recipe, Ingredient
from django.http import Http404
from rest_framework import status


# Define views for managing restaurants
class Restaurants(APIView):
    """
    This class defines views for managing restaurants.

    GET request: Retrieve all restaurants
    POST request: Create a new restaurant
    """

    def get(self, request):
        """
        GET request to retrieve all restaurants
        :param request: HTTP request
        :return: Response with all restaurants
        """
        restaurants = Restaurant.objects.all()
        serializer = serializers.RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST request to create a new restaurant
        :param request: HTTP request
        :return: Response with the new restaurant
        """
        serializer = serializers.RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define views for managing individual restaurants
class RestaurantDetail(APIView):
    """
    This class defines views for managing individual restaurants.

    GET request: Retrieve a specific restaurant by ID
    DELETE request: Delete a spexcific restaurant by ID
    PUT request: Update a specific restaurant by ID
    """

    def get(self, request, restaurant_id):
        """
        GET request to retrieve a specific restaurant by ID
        :param request: HTTP request
        :param restaurant_id: ID of the restaurant
        :return: Response with the restaurant
        :raises: Http404 if the restaurant does not exist
        """
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        serializer = serializers.RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def delete(self, request, restaurant_id):
        """
        DELETE request to delete a specific restaurant by ID
        :param request: HTTP request
        :param restaurant_id: ID of the restaurant
        :return: Response with status code
        :raises: Http404 if the restaurant does not exist

        """
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, restaurant_id):
        """
        PUT request to update a specific restaurant by ID
        :param request: HTTP request
        :param restaurant_id: ID of the restaurant
        :return: Response with the updated restaurant
        :raises: Http404 if the restaurant does not exist
        """
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
            serializer = serializers.RestaurantSerializer(restaurant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Restaurant.DoesNotExist:
            raise Http404


# Define views for managing recipes
class Recipes(APIView):
    """
    This class defines views for managing recipes.

    GET request: Retrieve all recipes
    POST request: Create a new recipe
    """

    def get(self, request):
        """
        GET request to retrieve all recipes
        :param request: HTTP request
        :return: Response with all recipes
        """
        recipes = Recipe.objects.all()
        serializer = serializers.RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST request to create a new recipe
        :param request: HTTP request
        :return: Response with the new recipe
        """
        serializer = serializers.RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):
    """
    This class defines views for managing individual recipes.

    GET request: Retrieve a specific recipe by ID
    DELETE request: Delete a specific recipe by ID
    PUT request: Update a specific recipe by ID
    """

    def get(self, request, recipe_id):
        """
        GET request to retrieve a specific recipe by ID
        :param request: HTTP request
        :param recipe_id: ID of the recipe
        :return: Response with the recipe
        :raises: Http404 if the recipe does not exist
        """
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        serializer = serializers.RecipeSerializer(recipe)
        return Response(serializer.data)

    def delete(self, request, recipe_id):
        """
        DELETE request to delete a specific recipe by ID
        :param request: HTTP request
        :param recipe_id: ID of the recipe
        :return: Response with status code
        :raises: Http404 if the recipe does not exist
        """
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, recipe_id):
        """
        PUT request to update a specific recipe by ID
        :param request: HTTP request
        :param recipe_id: ID of the recipe
        :return: Response with the updated recipe
        :raises: Http404 if the recipe does not exist
        """
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            serializer = serializers.RecipeSerializer(recipe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Recipe.DoesNotExist:
            raise Http404


class Ingredients(APIView):
    """
    This class defines views for managing ingredients.

    GET request: Retrieve all ingredients
    POST request: Create a new ingredient
    """

    def get(self, request):
        """
        GET request to retrieve all ingredients
        :param request: HTTP request
        :return: Response with all ingredients
        """
        ingredients = Ingredient.objects.all()
        serializer = serializers.IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST request to create a new ingredient
        :param request: HTTP request
        :return: Response with the new ingredient
        """
        serializer = serializers.IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetail(APIView):
    """
    This class defines views for managing individual ingredients.

    GET request: Retrieve a specific ingredient by ID
    DELETE request: Delete a specific ingredient by ID
    PUT request: Update a specific ingredient by ID
    """

    def get(self, request, ingredient_id):
        """
        GET request to retrieve a specific ingredient by ID
        :param request: HTTP request
        :param ingredient_id: ID of the ingredient
        :return: Response with the ingredient
        :raises: Http404 if the ingredient does not exist
        """
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist:
            raise Http404
        serializer = serializers.IngredientSerializer(ingredient)
        return Response(serializer.data)

    def delete(self, request, ingredient_id):
        """
        DELETE request to delete a specific ingredient by ID
        :param request: HTTP request
        :param ingredient_id: ID of the ingredient
        :return: Response with status code
        :raises: Http404 if the ingredient does not exist
        """
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
        except Ingredient.DoesNotExist:
            raise Http404
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, ingredient_id):
        """
        PUT request to update a specific ingredient by ID
        :param request: HTTP request
        :param ingredient_id: ID of the ingredient
        :return: Response with the updated ingredient
        :raises: Http404 if the ingredient does not exist
        """
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            serializer = serializers.IngredientSerializer(ingredient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ingredient.DoesNotExist:
            raise Http404


class RestaurantRecipes(APIView):
    """
    This class defines views for retrieving recipes associated with a specific restaurant.

    GET request: Retrieve recipes associated with a specific restaurant
    """

    def get(self, request, restaurant_id):
        """
        GET request to retrieve recipes associated with a specific restaurant
        :param request: HTTP request
        :param restaurant_id: ID of the restaurant
        :return: Response with the recipes
        :raises: Http404 if the restaurant does not exist
        """

        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
            recipes = Recipe.objects.filter(restaurant=restaurant)
            serializer = serializers.RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({"message": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)


class IngredientRecipes(APIView):
    """
    This class defines views for retrieving recipes associated with a specific ingredient.

    GET request: Retrieve recipes associated with a specific ingredient
    """

    def get(self, request, ingredient_id):
        """
        GET request to retrieve recipes associated with a specific ingredient
        :param request: HTTP request
        :param ingredient_id: ID of the ingredient
        :return: Response with the recipes
        :raises: Http404 if the ingredient does not exist
        """
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            recipes = ingredient.recipes.all()
            serializer = serializers.RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
        except Ingredient.DoesNotExist:
            return Response({"message": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)


class RestaurantIngredients(APIView):
    """
    This class defines views for retrieving ingredients associated with a specific restaurant.

    GET request: Retrieve ingredients associated with a specific restaurant
    """

    def get(self, request, restaurant_id):
        """
        GET request to retrieve ingredients associated with a specific restaurant
        :param request: HTTP request
        :param restaurant_id: ID of the restaurant
        :return: Response with the ingredients
        :raises: Http404 if the restaurant does not exist
        """
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
            recipes = Recipe.objects.filter(restaurant=restaurant)
            ingredients = Ingredient.objects.filter(recipes__in=recipes).distinct()
            serializer = serializers.IngredientSerializer(ingredients, many=True)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({"message": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)


class RestaurantsByRecipe(APIView):
    """
    This class defines views for retrieving restaurants associated with a specific recipe name.

    GET request: Retrieve restaurants associated with a specific recipe name
    """

    def get(self, request, recipe_name):
        """
        GET request to retrieve restaurants associated with a specific recipe name
        :param request: HTTP request
        :param recipe_name: name of the recipe
        :return: Response with the restaurants
        :raises: Http404 if the recipe does not exist
        """
        try:
            recipes = Recipe.objects.filter(name=recipe_name)
            restaurant_names = set()
            for recipe in recipes:
                restaurant_names.add(recipe.restaurant.name)
            restaurants = Restaurant.objects.filter(name__in=restaurant_names)
            serializer = serializers.RestaurantSerializer(restaurants, many=True)
            return Response(serializer.data)
        except Recipe.DoesNotExist:
            raise Http404("Recipe does not exist")


class RecipeIngredients(APIView):
    """
    This class defines views for retrieving ingredients associated with a specific recipe.
    """

    def get(self, request, recipe_id):
        """
        GET request to retrieve ingredients associated with a specific recipe
        :param request: HTTP request
        :param recipe_id: ID of the recipe
        :return: Response with the ingredients
        :raises: Http404 if the recipe does not exist
        """
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            ingredients = recipe.ingredients.all()
            serializer = serializers.IngredientSerializer(ingredients, many=True)
            return Response(serializer.data)
        except Recipe.DoesNotExist:
            return Response({"message": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)


class AllRecipes(APIView):
    """
    This class defines views for retrieving all recipes.

    GET request: Retrieve all recipes
    """

    def get(self, request):
        """
        GET request to retrieve all recipes
        :param request: HTTP request
        :return: Response with all recipes
        """
        recipes = Recipe.objects.all()
        serializer = serializers.RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


class AllIngredients(APIView):
    """
    This class defines views for retrieving all ingredients.

    GET request: Retrieve all ingredients
    """

    def get(self, request):
        """
        GET request to retrieve all ingredients
        :param request: HTTP request
        :return: Response with all ingredients
        """
        ingredients = Ingredient.objects.all()
        serializer = serializers.IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
