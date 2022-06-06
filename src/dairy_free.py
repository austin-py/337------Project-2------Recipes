
import ingredient_parser as ip 

dairy_types = {
    "milk": "oat milk",
    "butter": "plant based imitation butter",
    "cheese": "vegan cheese",
    "yogurt": "almond milk yogurt",
    "whey protien": "brown rice protien"
} 

ingreds = ip.get_ingredient_list('https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/')
for i in ingreds: 
    print (i.name)


def dairy_free(recipe):
    """
    Input: Takes a recipe object descriped in classes.py,
    
    Output: Returns the recipe with dairy products replaced. 
    """
    ingredients = recipe.ingredients
    for ingredient in ingredients:
        if ingredient.name in dairy_types.keys():
            ingredient.name = dairy_types[ingredient.name]
        for step in recipe.steps:
            if ingredient.name in step:
                step.replace(ingredient.name,dairy_types[ingredient.name])
        
    
    #TODO adjust general nutrition info 
    
    recipe.ingredients = ingredients 
    return recipe 


