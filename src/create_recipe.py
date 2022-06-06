from classes import * 
from soup import * 
from ingredient_parser import * 
from step_parser import get_directions as get_steps
from method_parser import * 

def create_recipe(url):
    rv = Recipe(url_to_name(url))
    data = get_soup_dictionary(url)
    rv.ingredients = get_ingredient_list(data)
    # rv.tools = 
    rv.methods = parse_method(data)
    rv.steps = get_steps(data)

    return rv 