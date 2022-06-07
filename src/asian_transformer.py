import copy
from classes import Recipe, Step
from step_parser import get_directions, print_directions
from read_json import load_recipe
import random
from create_recipe import create_recipe


def asianized(recipe):
    non_asian_foods = ['butter', 'cheese', 'Cheese', 'milk', 'noodles', 'liquor', 'green peppers', 'oil', 'vinegar',
                       'bacon', 'lasagna', 'wine', 'tomato sauce', 'tomato', 'jalapeno', 'ground beef', 'spaghetti',
                       'macaroni', 'rigatoni', 'pasta']
    asian_subs = {'butter': ['coconut oil'], 'cheese': ['soy cheese', 'tofu cheese'],
                  'Cheese': ['soy cheese', 'tofu cheese'], 'ground beef': ['beef strips'],
                  'milk': ['soy milk'], 'noodles': ['pad thai noodles', 'lo mein noodles'],
                  'lasagna': ['pad thai noodles', 'lo mein noodles'], 'macaroni': ['pad thai noodles', 'lo mein noodles'],
                  'spaghetti': ['pad thai noodles', 'lo mein noodles'], 'rigatoni': ['pad thai noodles', 'lo mein noodles'],
                  'liquor': ['sake', 'rice vinegar', 'rice wine'], 'wine': ['sake', 'rice vinegar', 'rice wine'], 'green peppers': ['green onions', 'shallots', 'celery'],
                  'oil': ['sesame seed oil'], 'vinegar':
                      ['rice vinegar'], 'bacon': ['pork loin'], 'tomato sauce': ['tomato sauce'], 'tomato': ['chilies'],
                  'jalapeno': ['chili sauce', 'ginger', 'chestnuts'], 'pasta': ['pad thai noodles', 'lo mein noodles']}

    transformed_recipe = copy.deepcopy(recipe)
    transformed_recipe.name = recipe.name + 'with, an Asian Twist'
    ingredients = transformed_recipe.ingredients

    for i in range(len(ingredients)):
        for food in non_asian_foods:
            if food in ingredients[i].name:
                ingredients[i].name = random.choice(asian_subs[food])
    res = []
    taken = []
    for x in ingredients:
        if x.name not in taken:
            res.append(x)
            taken.append(x.name)
    transformed_recipe.ingredients = res
    return transformed_recipe


def main():
    links = ['https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/',
             'https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/',
             'https://www.allrecipes.com/recipe/16167/beef-bourguignon-i/',
             'https://www.allrecipes.com/recipe/228285/teriyaki-salmon/',
             'https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/',
             'https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/',
             'https://www.allrecipes.com/recipe/73303/mexican-rice-iii/']
    recipe = create_recipe(links[0])
    asian_recipe = asianized(recipe)
    for ingredient in asian_recipe.ingredients:
        print(ingredient.name)


if __name__ == '__main__':
    main()