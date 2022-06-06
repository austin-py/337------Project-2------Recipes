from classes import *
from read_json import load_recipe
from soup import *

from_vege_dict = {
    'tofu' : ['steak', 'fish', 'trout', 'fillet', 'cod', 'halibut'],
    'seitan': ['beef', 'turkey', 'pork', 'ham' ],
    'lentil': ['bacon', 'sausage', 'ham'],
    'shiitake mushroom': ['shrimp', 'crab', 'lobster'],
    'jackfruit' : ['octopus', 'squid'],
    'mushroom': ['pork']
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
                    replacement_dict[curr_name] = k
                    change += '   {} --> {}\n'.format(curr_name, k)
                    recipe.ingredients[i] = k
                    added_ingredient.append(k)
                    if 'ground' in curr_name:
                        temp_step = create_crush_step(k, extra_steps)
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
        s.step_number += len(extra_steps)
        for i in range(len(s.ingredients)):
            if s.ingredients[i] in replacement_dict.keys():
                s.ingredients[i] = replacement_dict[s.ingredients[i]]

    recipe.steps = extra_steps + recipe.steps
    return recipe, change


def create_crush_step(k, extra_steps):
    temp_step = Step(len(extra_steps) + 1)
    temp_step.ingredients.append(k)
    temp_step.tools.append('mortar')
    if 'mortar' not in recipe.tools:
        recipe.tools.append('mortar')
    temp_step.methods.append('crush')
    temp_step.time = ['5 minutes']
    return temp_step
