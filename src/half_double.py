from src import ingredient_parser as ip 
from src.classes import Recipe


def scale_recipe(recipe, scale_factor):
    """
    Input: Takes a recipe object descriped in classes.py, and a float scale factor
    
    Output: Returns the recipe scaled by the factor 
    """
    ingredients = recipe.ingredients
    for ingredient in ingredients:
        ingredient.quantity *= scale_factor

    #TODO cut nutrition info and serving size in half too 

    
    recipe.ingredients = ingredients 
    return recipe 


