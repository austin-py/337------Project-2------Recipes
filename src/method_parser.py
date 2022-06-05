from classes import *
from read_json import load_recipe
from soup import *

def parse_method(data):
    all_directions = ''
    for d in data['directions']:
        all_directions += d
    for i in data['ingredients']:
        all_directions += i
    all_directions = all_directions.lower()
    all_main_methods = {
        'broil': ['broil'],
        'stir fry': ['stir-fry', 'stir fry', 'stir fried', 'stir-fried'],
        'saute': ['saute', 'sauté'],
        'braise': ['braise', 'braising'],
        'sear' : ['sear'],
        'grill' : ['grill'],
        'roast': ['roast'],
        'simmer': ['simmer'],
        'poach': ['poach'],
        'boil': ['boil'],
        'bake': ['bake', 'baking'],
        'deep fry': ['deep-fry', 'deep fry', 'deep fried', 'deep-fried'],
        'stew': ['stew'],
        'steam': ['steam'],
        'broil': ['broil'],
        'blanch': ['blanch'],
        'sous vide': ['sous vide', 'sous-vide'],
        'shallow fry': ['shallow-fry', 'shallow fry', 'shallow fried', 'shallow-fried'],
        'fry': ['fry', 'fried']
    }

    all_secondary_methods = ['cut', 'chop', 'slice', 'shred', 'dice', 'divide',
                             'mince', 'crush', 'blend', 'squeeze', 'peel',
                             'stir', 'mix', 'whisk', 'drain', 'strain', 'marinate',
                             'brush',
                             'freeze', 'cool', 'caramelize', 'preheat']

    returned_main_methods = []
    for k in all_main_methods.keys():
        all_variation = all_main_methods[k]
        for v in all_variation:
            if v in all_directions:
                returned_main_methods.append(k)
                break

    returned_sec_methods = []
    for m in all_secondary_methods:
        if m in all_directions:
            returned_sec_methods.append(m)
    return returned_main_methods, returned_sec_methods

def test_method_parser():
    links = ['https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/',
            'https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/',
            'https://www.allrecipes.com/recipe/16167/beef-bourguignon-i/',
            'https://www.allrecipes.com/recipe/228285/teriyaki-salmon/',
            'https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/',
            'https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/',
            'https://www.allrecipes.com/recipe/73303/mexican-rice-iii/']
    for l in links:
        data = get_soup_dictionary(l)
        res = parse_method(data)
        print(res[0])
        print(res[1])

if __name__=='__main__':
    test_method_parser()
