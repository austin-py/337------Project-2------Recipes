from classes import *
from read_json import load_recipe
from read_list import get_tool_list
import re
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
    recipe.tools = get_tool_list()
    print(recipe.tools)

    for d in directions:
        match = re.search(r'\d\s', d)
        text = d.replace(match.group(0), '')
        text = text.replace('Step ', '')
        for w in text.split():
            for t in recipe.tools:
                if w.lower() == t.lower():
                    print(w)

    return directions


def main():
    get_directions()

if __name__=='__main__':
    main()