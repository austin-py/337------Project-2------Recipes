
import ingredient_parser as ip 
from create_recipe import create_recipe

dairy_types = {
    "milk": "oat milk",
    "butter": "plant based imitation butter",
    "cheese": "vegan cheese",
    "yogurt": "almond milk yogurt",
    "whey protien": "brown rice protien"
} 
def dairy_free(recipe):
    """
    Input: Takes a recipe object descriped in classes.py,
    
    Output: Returns the recipe with dairy products replaced. 
    """
    ingredients = recipe.ingredients
    for ingredient in ingredients:
        for dairy in dairy_types.keys():
            if dairy in ingredient.name:
                ingredient.name = ingredient.name.replace(dairy,dairy_types[dairy])
    
    steps = recipe.steps
    for step in steps:  
        for dairy in dairy_types.keys():
            if dairy in step.description:
                step.description = step.description.replace(dairy,dairy_types[dairy])

    recipe.ingredients = ingredients
    recipe.steps = steps 
     #TODO adjust general nutrition info 
    return recipe 
        
    
   


if __name__ == '__main__':
    recipe = create_recipe('https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/')
    for i in recipe.ingredients:
        print (i.name)

    dairy_f = dairy_free(recipe)

    for i in dairy_f.ingredients:
        print (i.name)

