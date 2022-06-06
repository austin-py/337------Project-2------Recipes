from classes import *
from read_json import load_recipe
from soup import *
import create_recipe as cr

from_vege_dict = {
    'tofu' : ['ground beef', 'steak', 'ground turkey', 'ground pork', 'fish', 'trout', 'fillet', 'cod', 'halibut'],
    'seitan': ['beef', 'turkey', 'pork', 'ham'],
    'lentil': ['bacon', 'sausage', 'ham'],
    'shiitake mushroom': ['shrimp', 'crab', 'lobster'],
    'jackfruit' : ['octopus', 'squid'],
    'mushroom': ['ground pork', 'pork']
}


def to_vegetarian(recipe):
    change = 'Ingredient changes:\n'
    added_ingredient = []
    extra_steps = []
    replacement_dict = {}
    for i in range(len(recipe.ingredients)):
        curr_name = recipe.ingredients[i].name.lower()
        for k in from_vege_dict.keys():
            stop = False
            for r in from_vege_dict[k]:
                if r in curr_name:
                    stop  = True
                    replacement_dict[curr_name] = curr_name.replace(r, k)
                    recipe.ingredients[i].name = replacement_dict[curr_name]
                    change += '   {} --> {}\n'.format(curr_name, replacement_dict[curr_name])

                    added_ingredient.append(k)
                    if 'ground' in curr_name:
                        temp_step = create_crush_step(k, extra_steps, recipe)
                        if 'crush' not in recipe.methods[1]:
                            recipe.methods[1].append('crush')
                        extra_steps.append(temp_step)
                    break
            if stop:
                break


    change += '\nStep Added:\n'

    for step in extra_steps:
        change += '   Step {}:\n'.format(step.step_number)
        change += '      Ingredients: {}\n'.format(step.ingredients)
        change += '      Tools: {}\n'.format(step.tools)
        change += '      Methods: {}\n'.format(step.methods)
        change += '      Times: {}\n'.format(step.time)

    for s in recipe.steps:
        s.step_number = str(int(s.step_number) + len(extra_steps))
        for i in range(len(s.ingredients)):
            if s.ingredients[i] in replacement_dict.keys():
                s.ingredients[i] = replacement_dict[s.ingredients[i]]

    recipe.steps = extra_steps + recipe.steps
    return recipe, change

def to_non_vegetarian(recipe):
    change = 'Ingredient changes:\n'
    added_ingredient = []
    extra_steps = []
    replacement_dict = {}
    for i in range(len(recipe.ingredients)):
        curr_name = recipe.ingredients[i].name.lower()
        for k in from_vege_dict.keys():
            if k in curr_name:
                recipe.ingredients[i].name = from_vege_dict[k][0]
                replacement_dict[curr_name] = from_vege_dict[k][0]
                change += '   {} --> {}\n'.format(curr_name, replacement_dict[curr_name])

    for s in recipe.steps:
        for i in range(len(s.ingredients)):
            if s.ingredients[i] in replacement_dict.keys():
                s.ingredients[i] = replacement_dict[s.ingredients[i]]

    recipe.steps = extra_steps + recipe.steps
    return recipe, change

def create_crush_step(k, extra_steps, recipe):
    temp_step = Step(len(extra_steps) + 1)
    temp_step.ingredients.append(k)
    temp_step.tools.append('mortar')
    if 'mortar' not in recipe.tools:
        recipe.tools.append('mortar')
    temp_step.methods.append('crush')
    temp_step.time = ['5', 'minutes']
    return temp_step


def test_vege():
    url = 'https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/'
    recipe = cr.create_recipe(url)
    new_recipe, change = to_vegetarian(recipe)
    print(change)
    new_recipe.print_recipe()

    url = 'https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/'
    recipe = cr.create_recipe(url)
    new_recipe, change = to_non_vegetarian(recipe)
    print(change)
    new_recipe.print_recipe()

if __name__=='__main__':
    test_vege()