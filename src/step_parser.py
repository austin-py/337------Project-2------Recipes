from classes import *
from read_json import load_recipe
from read_list import get_kichen_utensils_list
'''
self.step_number = number
self.ingredients = []
self.tools = []
self.methods = []
self.time = 0
self.description = ''
'''

def get_directions(filename=None):
    recipe_data = load_recipe(filename)
    recipe_name = recipe_data['Recipe Name']
    directions = recipe_data['directions']
    recipe = Recipe(recipe_name)
    recipe.tools = get_kichen_utensils_list()
    print(recipe.tools)
    return directions


def main():
    print(get_directions())

if __name__=='__main__':
    main()