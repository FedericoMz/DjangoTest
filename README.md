# DjangoTest
 A simple app I made to learn Django, managing restaurants, recipes, and ingredients.

## Requirements
 You must set up a Postgres Server, and edit the file _settings.py_ accordingly.

## APIs
 The app employs the following APIs to manage restaurants, recipes, and ingredients. They provide endpoints for various CRUD operations. The Notebook file provides some examples.

1. **Restaurants API:**
   - Endpoint: `/restaurants/`
   - Methods:
     - `GET`: Retrieves all restaurants.
     - `POST`: Creates a new restaurant.

2. **Restaurant Detail API:**
   - Endpoint: `/restaurants/<restaurant_id>/`
   - Methods:
     - `GET`: Retrieves a specific restaurant by ID.
     - `PUT`: Updates a specific restaurant by ID.
     - `DELETE`: Deletes a specific restaurant by ID.

3. **Recipes API:**
   - Endpoint: `/recipes/`
   - Methods:
     - `GET`: Retrieves all recipes.
     - `POST`: Creates a new recipe.

4. **Recipe Detail API:**
   - Endpoint: `/recipes/<recipe_id>/`
   - Methods:
     - `GET`: Retrieves a specific recipe by ID.
     - `PUT`: Updates a specific recipe by ID.
     - `DELETE`: Deletes a specific recipe by ID.

5. **Ingredients API:**
   - Endpoint: `/ingredients/`
   - Methods:
     - `GET`: Retrieves all ingredients.
     - `POST`: Creates a new ingredient.

6. **Ingredient Detail API:**
   - Endpoint: `/ingredients/<ingredient_id>/`
   - Methods:
     - `GET`: Retrieves a specific ingredient by ID.
     - `PUT`: Updates a specific ingredient by ID.
     - `DELETE`: Deletes a specific ingredient by ID.

7. **Restaurant Recipes API:**
   - Endpoint: `/restaurants/<restaurant_id>/recipes/`
   - Method:
     - `GET`: Retrieves recipes associated with a specific restaurant.

8. **Ingredient Recipes API:**
   - Endpoint: `/ingredients/<ingredient_id>/recipes/`
   - Method:
     - `GET`: Retrieves recipes associated with a specific ingredient.

9. **Restaurant Ingredients API:**
   - Endpoint: `/restaurants/<restaurant_id>/ingredients/`
   - Method:
     - `GET`: Retrieves ingredients associated with a specific restaurant.

10. **Restaurants By Recipe API:**
    - Endpoint: `/recipes/<recipe_name>/restaurants/`
    - Method:
      - `GET`: Retrieves restaurants associated with a specific recipe name.

11. **Recipe Ingredients API:**
    - Endpoint: `/recipes/<recipe_id>/ingredients/`
    - Method:
      - `GET`: Retrieves ingredients associated with a specific recipe.

12. **All Recipes API:**
    - Endpoint: `/all-recipes/`
    - Method:
      - `GET`: Retrieves all recipes.

13. **All Ingredients API:**
    - Endpoint: `/all-ingredients/`
    - Method:
      - `GET`: Retrieves all ingredients.
