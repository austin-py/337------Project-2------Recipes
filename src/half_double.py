from create_recipe import * 


def scale_recipe(recipe, scale_factor):
    """
    Input: Takes a recipe object descriped in classes.py, and a float scale factor
    
    Output: Returns the recipe scaled by the factor 
    """
    recipe.name += " scaled by {}".format(scale_factor)
    ingredients = recipe.ingredients
    for ingredient in ingredients:
        ingredient.quantity *= scale_factor

    
    recipe.ingredients = ingredients 
    return recipe 


if __name__ == '__main__':
    recipe = create_recipe('https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/')
    for i in recipe.ingredients:
        print (i.name,i.quantity)

    dairy_f = scale_recipe(recipe,.5)
    print(recipe.name)

    for i in dairy_f.ingredients:
        print (i.name, i.quantity)
