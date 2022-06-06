from classes import *
from soup import *
import re
import nltk


def parse_ingredient(data):

    measurements = {'teaspoon': ['teaspoon', 'teaspoons', 'teaspoon of', 'teaspoons of'],
                    'tablespoon': ['tablespoon', 'tablespoons', 'tablespoon of', 'tablespoons of'],
                    'ounce': ['ounce', 'ounces', 'ounces of', 'ounce of', 'oz'],
                    'clove': ['clove', 'cloves', 'cloves of', 'cloves of'],
                    'cup': ['cup', 'cups', 'cup of', 'cups of'], 'pound': ['pound', 'lbs', 'lb', 'pounds'],
                    'gram': ['gram', 'grams']}

    remove_from_name = {'can': ['can', 'can of', 'cans', 'cans of'], 'jar': ['jar', 'jar of', 'jars', 'jars of'],
                        'container': ['container', 'container of', 'containers', 'containers of'],
                        'packet': ['packet', 'packets', 'packet of', 'packets of'],
                        'package': ['package', 'packages', 'packages of', 'package of'], 'box': ['box', 'boxes']}

    descriptor_dict = {'small': ['small'], 'large': ['large'], 'fresh': ['fresh'], 'dried': ['dried'],
                       'cured': ['cured'], 'smoked': ['smoked'], 'raw': ['raw'],
                       'precooked': ['precooked', 'pre-cooked'], 'preheated': ['preheated', 'pre-heated'], 'all-purpose': ['all-purpose', 'all purpose'],
                       'ground': ['ground'], 'dry': ['dry'], 'fermented': ['fermented']}

    ingredients_list = data['ingredients']
    measurement_in_parentheses = {}
    quantities_output = []
    measurements_output = []
    name_output = []
    preparation_output = []
    descriptor_output = []

    for i in range(len(ingredients_list)):
        result = re.search(r"\([^)]*\)", ingredients_list[i])
        if result:
            pair = result.group()
            pair = pair.replace('(', '')
            pair = pair.replace(')', '')
            pair = pair.split(' ')
            if len(pair) == 2:
                measurement_in_parentheses[i] = (pair[0], pair[1])
            ingredients_list[i] = ingredients_list[i].replace(result.group(), '')

    ingredient_listss = []
    for ingredient in ingredients_list:
        ingredient_listss.append(list(filter(('').__ne__, ingredient.split(' '))))
    for il in ingredient_listss:
        quantity = 0
        measurement = 'None Given'
        mqtpl = distr_components(il, ingredient_listss, quantity, measurement, measurement_in_parentheses, measurements)
        quantities_output.append(mqtpl[1])
        measurements_output.append(mqtpl[0])
        descriptor = ''
        for key in descriptor_dict.keys():
            for word in descriptor_dict[key]:
                if word in il:
                    if descriptor == '':
                        descriptor += word
                    else:
                        descriptor += f' and {word}'
        if descriptor == '':
            descriptor = 'None Given'
        descriptor_output.append(descriptor)
        for key in remove_from_name.keys():
            for word in remove_from_name[key]:
                if word in il:
                    il.remove(word)
        il_word = ' '.join(il)
        text = nltk.word_tokenize(il_word)
        pos_tagged = nltk.pos_tag(text)
        name = ''
        preparation = ''
        for tpl in pos_tagged:
            if tpl[1] == 'NN' or tpl[1] == 'JJ' or tpl[1] == 'NNS' or tpl[1] == 'VB' or tpl[1] == 'NNP':
                if name == '':
                    name += f'{tpl[0]}'
                else:
                    name += f' {tpl[0]}'
            elif tpl[1] == 'VBD' or tpl[1] == 'VBN':
                if preparation == '':
                    preparation += f'{tpl[0]}'
                else:
                    preparation += f' and {tpl[0]}'
        if mqtpl[0] == 'None Given':
            measurements_output[ingredient_listss.index(il)] = name
        if preparation == '':
            preparation = 'untouched'
        name_output.append(name)
        preparation_output.append(preparation)
    return name_output, quantities_output, measurements_output, descriptor_output, preparation_output
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
                # print(il)
                # print(measurement, quantity)
                return measurement, quantity
            for fk in fractions.keys():
                if fk in initial_digit:  # fk could be inside initial_digit, if its a mixed number
                    quantity = fractions[fk] + float(whole_number)
                    break
        else:
            quantity += fractions[initial_digit]
    else:
        quantity += int(initial_digit)
    il.remove(initial_digit)
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
                    il.remove(variation)
                    break_flag = 1
                    break
            if break_flag == 1:
                break
    # print(il)
    # print(measurement, quantity)
    return measurement, quantity
def test_ingredient_parser():
    links = ['https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/',
             'https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/',
            'https://www.allrecipes.com/recipe/16167/beef-bourguignon-i/',
            'https://www.allrecipes.com/recipe/228285/teriyaki-salmon/',
            'https://www.allrecipes.com/recipe/229293/korean-saewoo-bokkeumbap-shrimp-fried-rice/',
            'https://www.allrecipes.com/recipe/7757/tiramisu-cheesecake/',
            'https://www.allrecipes.com/recipe/73303/mexican-rice-iii/']
    answer = []
    for l in links:
        data = get_soup_dictionary(l)
        ingredient_class_list = []
        ingredient_tuple = parse_ingredient(data)
        for i in range(len(ingredient_tuple[0])):
            iclm = Ingredient(ingredient_tuple[0][i], ingredient_tuple[1][i], ingredient_tuple[2][i],
                              ingredient_tuple[3][i], ingredient_tuple[4][i])
            print(f"NAME: {iclm.name}, QUANTITY: {iclm.quantity}, UNIT: {iclm.measurement}, "
                  f"DESCRIPTION: {iclm.descriptor}, PREP: {iclm.preparation} | FROM: {data['ingredients'][i]}")

            ingredient_class_list.append(iclm)
        answer.append(ingredient_class_list)
    return answer
        #res = parse_ingredient(data)
        #print(res[0])
        #print(res[1])

def get_ingredient_list(data):
    """
    Takes a data dictionary from Allrecipes.com and returns a list of ingredient objects for further manipulation. 
    """
    ingredient_class_list = []
    ingredient_tuple = parse_ingredient(data)
    for i in range(len(ingredient_tuple[0])):
        iclm = Ingredient(ingredient_tuple[0][i], ingredient_tuple[1][i], ingredient_tuple[2][i],
                          ingredient_tuple[3][i], ingredient_tuple[4][i])
        ingredient_class_list.append(iclm)
    return ingredient_class_list


if __name__ == '__main__':
    test_ingredient_parser()
