import json
import sys

# read json to dict
def load_recipe(filename=None):
    if not filename:
        filename = 'recipe_data.json'
    path = '../Data/' + filename
    print('Reading {}'.format(filename))
    with open(path) as recipe_file:
        recipe = json.load(recipe_file)
    print('Finish reading {}'.format(filename))
    #print('Number of entries: {}'.format(len(recipe)))
    #print(recipe)
    return recipe

def main(*args):
    #you can use terminal to run the script e.g., python json_read.py 'gg2013'
    print('Running {}'.format(sys.argv[0]))
    load_recipe()
    print('Finish running {}'.format(sys.argv[0]))


if __name__ == '__main__':
    main()