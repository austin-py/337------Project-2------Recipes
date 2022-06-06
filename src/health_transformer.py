from classes import Recipe, Step
from step_parser import get_directions, print_directions
from read_json import load_recipe
import random
from create_recipe import create_recipe

healthy_protein_list = ['chicken', 'salmon', 'tilapia', 'turkey', 'tofu', 'beans']
unhealthy_protein_list = ['bacon', 'sausage', 'ham', 'salami']
healthy_condiment_list = ['maple syrup', 'raw honey', 'almond butter', 'apple cider vinegar', 'olive oil']
unhealthy_condiment_list = ['brown sugar','sugar', 'mayo', 'ketchup', 'honey mustard', 'soy sauce', 'hot sauce', 'chocolate syrup']
healthy_method_list = ['broil', 'bake', 'poach', 'steam']
unhealthy_method_list = ['cure', 'deep fry', 'caramelize', 'grill', 'roast', 'stir fry']

def to_healthy(recipe):
    recipe.name = 'healthy ' + recipe.name
    ingredients = recipe.ingredients

    for i in range(len(ingredients)):
        if ingredients[i].name in unhealthy_protein_list:
            ingredients[i].name = random.choice(healthy_protein_list)
        elif ingredients[i].name in unhealthy_condiment_list:
            ingredients[i].name = random.choice(healthy_condiment_list)

        ingredients[i].name = 'organic ' + ingredients[i].name

    recipe.ingredients = ingredients
    steps = recipe.steps
    for s in steps:
        for i in range(len(s.ingredients)):
            if s.ingredients[i] in unhealthy_protein_list:
                s.ingredients[i] = random.choice(healthy_protein_list)
            elif s.ingredients[i] in unhealthy_condiment_list:
                s.ingredients[i] = random.choice(healthy_condiment_list)

            s.ingredients[i] = 'organic ' + s.ingredients[i]

        for i in range(len(s.methods)):
            if s.methods[i] in unhealthy_method_list:
                s.methods[i] = random.choice(healthy_method_list)
    recipe.steps = steps

    return recipe

def to_unhealthy(recipe):
    recipe.name = 'unhealthy ' + recipe.name
    ingredients = recipe.ingredients
    for i in range(len(ingredients)):
        if ingredients[i].name in healthy_protein_list:
            ingredients[i].name = random.choice(unhealthy_protein_list)
        elif ingredients[i].name in healthy_condiment_list:
            ingredients[i].name = random.choice(unhealthy_condiment_list)

        ingredients[i].name = 'inorganic ' + ingredients[i].name
    recipe.ingredients = ingredients
    steps = recipe.steps
    for s in steps:
        for i in range(len(s.ingredients)):
            if s.ingredients[i] in healthy_protein_list:
                s.ingredients[i] = random.choice(unhealthy_protein_list)
            elif s.ingredients[i] in healthy_condiment_list:
                s.ingredients[i] = random.choice(unhealthy_condiment_list)

            s.ingredients[i] = 'inorganic ' + s.ingredients[i]

        for i in range(len(s.methods)):
            if s.methods[i] in healthy_method_list:
                s.methods[i] = random.choice(unhealthy_method_list)

    recipe.steps = steps

    return recipe

def main():
    links = ['https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/',
             'https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/',
             'https://www.allrecipes.com/recipe/16167/beef-bourguignon-i/',
             'https://www.allrecipes.com/recipe/228285/teriyaki-salmon/',
             'https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/',
             'https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/',
             'https://www.allrecipes.com/recipe/73303/mexican-rice-iii/']
    recipe = create_recipe(links[0])
    print_directions(to_healthy(recipe).steps)

if __name__ == '__main__':
    main()