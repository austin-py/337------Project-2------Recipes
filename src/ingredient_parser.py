from src.classes import *
from src.read_json import load_recipe
from src.soup import *
import numpy as np
import re


def parse_ingredient(data):
    measurements = {'teaspoon': ['teaspoon', 'teaspoons', 'teaspoon of', 'teaspoons of'],
                    'tablespoon': ['tablespoon', 'tablespoons', 'tablespoon of', 'tablespoons of'],
                    'ounce': ['ounce', 'ounces', 'ounces of', 'ounce of', 'oz'],
                    'clove': ['clove', 'cloves', 'cloves of', 'cloves of'],
                    'cup': ['cup', 'cups', 'cup of', 'cups of'], 'pound': ['pound', 'lbs', 'lb', 'pounds'],
                    'gram': ['gram', 'grams']}

    remove_from_name = {'can': ['can of', 'cans', 'cans of'], 'jar': ['jar of', 'jars', 'jars of'],
                        'container': ['container of', 'containers', 'containers of'], 'grated': ['grated'],
                        'small': ['small'], 'large': ['large']}

    ingredients_list = data['ingredients']
    measurement_in_parentheses = {}

    for i in range(len(ingredients_list)):
        result = re.search(r"\([^)]*\)", ingredients_list[i])
        if result:
            pair = result.group()
            pair = pair.replace('(', '')
            pair = pair.replace(')', '')
            pair = pair.split(' ')
            if len(pair) == 2:
                measurement_in_parentheses[i] = (pair[0], pair[1])

    ingredient_listss = []
    for ingredient in ingredients_list:
        ingredient_listss.append(list(filter(('').__ne__, ingredient.split(' '))))
    for il in ingredient_listss:
        quantity = 0
        measurement = 'None Given'
        distr_components(il, ingredient_listss, quantity, measurement, measurement_in_parentheses, measurements)


def distr_components(il, ingredient_listss, quantity, measurement, measurement_in_parentheses, measurements):
    initial_digit = il[0]
    try:
        int(initial_digit)
    except:
        # if a fraction is in one of ingredient's words, get that word, take word[0]:
        # if word[0] = fraction: set ingredient quantity to fraction
        # else: isolate it in var, set ingredient quantity to value of fraction + var
        fractions = {'½': 0.5, '¼': 0.25}
        if initial_digit not in fractions:
            whole_number = initial_digit[0]
            if "to" in il and "taste" in il:
                quantity = "to taste"
                print(il)
                print(measurement, quantity)
                return
            for fk in fractions.keys():
                if fk in initial_digit:  # fk could be inside initial_digit, if its a mixed number
                    quantity = fractions[fk] + float(whole_number)
                    break
        else:
            quantity += fractions[initial_digit]
    else:
        quantity += int(initial_digit)
    if ingredient_listss.index(il) in measurement_in_parentheses.keys():
        ind = ingredient_listss.index(il)
        quantity *= float(measurement_in_parentheses[ind][0])
        measurement = measurement_in_parentheses[ind][1]
    else:
        break_flag = 0
        for m in measurements.keys():
            for variation in measurements[m]:
                if variation in il:
                    measurement = m
                    break_flag = 1
                    break
            if break_flag == 1:
                break
    print(il)
    print(measurement, quantity)

def test_ingredient_parser():
    links = ['https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/',
             'https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/',
            'https://www.allrecipes.com/recipe/16167/beef-bourguignon-i/',
            'https://www.allrecipes.com/recipe/228285/teriyaki-salmon/',
            'https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/',
            'https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/',
            'https://www.allrecipes.com/recipe/73303/mexican-rice-iii/']

    for l in links:
        data = get_soup_dictionary(l)
        parse_ingredient(data)
        #res = parse_ingredient(data)
        #print(res[0])
        #print(res[1])


if __name__ == '__main__':
    test_ingredient_parser()
