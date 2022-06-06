from classes import Recipe, Step
from step_parser import get_directions, ingredient_parser, print_directions
from read_json import load_recipe
import random

healthy_protein_list = ['chicken', 'salmon', 'tilapia', 'turkey', 'tofu', 'beans']
unhealthy_protein_list = ['bacon', 'sausage', 'ham', 'salami']
healthy_condiment_list = ['maple syrup', 'raw honey', 'almond butter', 'apple cider vinegar', 'olive oil']
unhealthy_condiment_list = ['brown sugar','sugar', 'mayo', 'ketchup', 'honey mustard', 'soy sauce', 'hot sauce', 'chocolate syrup']
healthy_method_list = ['broil', 'bake', 'poach', 'steam']
unhealthy_method_list = ['cure', 'deep fry', 'caramelize', 'grill', 'roast', 'stir fry']

def to_healthy(recipe_data):
    name = 'healthy ' + recipe_data['Recipe Name']
    ingredients = ingredient_parser(recipe_data['ingredients'])
    for i in range(len(ingredients)):
        if ingredients[i] in unhealthy_protein_list:
            ingredients[i] = random.choice(healthy_protein_list)
        if ingredients[i] in unhealthy_condiment_list:
            ingredients[i] = random.choice(healthy_condiment_list)
        if ingredients[i] in unhealthy_method_list:
            ingredients[i] = random.choice(healthy_method_list)

        ingredients[i] = 'organic ' + ingredients[i]
    recipe_data['ingredients'] = ingredients
    steps = get_directions(recipe_data)
    for s in steps:
        for i in range(len(s.methods)):
            if s.methods[i] in unhealthy_method_list:
                s.methods[i] = random.choice(healthy_method_list)

    return steps

def to_unhealthy(recipe_data):
    name = 'unhealthy ' + recipe_data['Recipe Name']
    ingredients = ingredient_parser(recipe_data['ingredients'])
    print(ingredients)
    for i in range(len(ingredients)):
        if ingredients[i] in healthy_protein_list:
            ingredients[i] = random.choice(unhealthy_protein_list)
        if ingredients[i] in healthy_condiment_list:
            ingredients[i] = random.choice(unhealthy_condiment_list)

        ingredients[i] = 'inorganic ' + ingredients[i]
    print(ingredients)
    recipe_data['ingredients'] = ingredients
    steps = get_directions(recipe_data)
    for s in steps:
        for i in range(len(s.methods)):
            if s.methods[i] in healthy_method_list:
                s.methods[i] = random.choice(unhealthy_method_list)

    return steps

def main():
    recipe_data = load_recipe()
    print_directions(to_unhealthy(recipe_data))

if __name__ == '__main__':
    main()