from classes import *
from read_json import load_recipe
from read_list import get_tool_list
import re
from method_parser import parse_method
'''
self.step_number = number
self.ingredients = []
self.tools = []
self.methods = []
self.time = 0
self.description = ''
'''


def get_directions(recipe_data):
    directions = recipe_data['directions']
    #Remove advertisement
    directions[0] = directions[0].replace('Advertisement', '')
    tools = get_tool_list()
    methods = parse_method(recipe_data)
    ingredients = recipe_data['ingredients']
    ingredients = ingredient_parser(ingredients)
    #print(ingredients)
    #print(tools)
    #print(methods)

    steps = []
    for d in directions:
        # match = re.search(r'\d\s', d)
        # text = d.replace(match.group(0), '')
        # text = text.replace('Step ', '')
        # for w in text.split():
        #     for t in tools:
        #         if w.lower() == t.lower():
        #             print(w)
        words = d.split()
        step_number = words[1]
        step = Step(step_number)
        #start location after step n to substring:
        start = d.index(words[2])
        d = d[start:]
        sentences = split_into_sentences(d)
        for s in sentences:
            #print(step_number + '' + s)
            step_ingredients = get_ingredients(s, ingredients)
            step_tools = get_tools(s, tools)
            step_methods = get_methods(s, methods)
            step_time = get_time(s)
            #print(s)
            #if step_time: print(step_time)
            #print(step_ingredients)
            #print(step_tools)
            #print(step_methods)
            #words = d.split()
            if step_ingredients:
                step.ingredients = list(set(step.ingredients + step_ingredients))
            if step_tools:
                step.tools = list(set(step.tools + step_tools))
            if step_methods:
                step.methods = list(set(step.methods + step_methods))
            if not step.time:
                step.time = step_time

        steps.append(step)
    return steps

#split sentences in a step by period '.'
def split_into_sentences(d):
    d = d.strip()
    results = d.split('.')
    #remove '' empty string from list
    while '' in results:
        results.remove('')

    return results

def ingredient_parser(ingredients):
    ingredients_list = []
    for i in ingredients:
        if len(i.split(',')) > 2:
            print('More than 1 comma: ' + i)
            return -1
        i = i.split(',')[0].lower()
        if ')' in i:
            #Just handle: "    4 (6 ounce) salmon steaks    ", it parses as 'steaks'
            if 'salmon steaks' in i:
                i = 'salmon steaks'
            else:
                start = i.index(')')
                i = i[start+1:]
                words = i.split()
                #skip quantity unit
                start = i.index(words[0]) + len(words[0])
                i = i[start:]
        else:
            words = i.split()
            if len(words) < 2:
                print('Unexpected length of ingredients:' + len(words))
                return -1

            if len(words) == 2:
                i = words[1]
            else:
                #skip qunatity unit
                if words[0].isdigit() or re.search(r'[\u00bc-\ua835]', words[0]):
                    if re.search(r'[\u00bc-\ua835]', words[1]):
                        quantity = (words[2])
                        start = i.index(words[3])
                    else:
                        #exception for noodles:
                        if 'noodles' in i:
                            start = i.index(words[1])
                        else:
                            start = i.index(words[2])
                else:
                    print('No quantity found: ' + i)
                    #To do: handle ' salt and pepper to taste'
                    start = 0
                    #return -1
                #start = i.index(words[0]) + len(words[0])
                i = i[start:]

        # skip flavor
        if 'flavored' in i:
            start = i.index('flavored') + len('flavored')
            i = i[start:]

        i = i.strip()
        ingredients_list.append(i)

    return ingredients_list

def get_ingredients(s, ingredients):
    ingredients_in_s = []
    for i in ingredients:
        for word in i.split():
            word = word.replace(',', '')
            word = word.replace('.', '')
            word = word.lower()
            if word in s.lower():
                if not i in ingredients_in_s:
                    ingredients_in_s.append(i)

    if not ingredients_in_s:
        #handle marinade
        if 'marinade' in s.lower():
            ingredients_in_s.append('marinade')

    return ingredients_in_s

def get_tools(s, tools):
    tools_in_s = []
    for s_w in s.split():
        s_w = s_w.replace(',', '')
        s_w = s_w.replace('.', '')
        s_w = s_w.lower()
        if s_w in tools:
            if not s_w in tools_in_s:
                tools_in_s.append(s_w)

    return tools_in_s

def get_methods(s, methods):
    methods_in_s = []
    for s_w in s.split():
        s_w = s_w.replace(',', '')
        s_w = s_w.replace('.', '')
        s_w = s_w.lower()
        if s_w in methods[0]:
            if not s_w in methods_in_s:
                methods_in_s.append(s_w)
        elif s_w in methods[1]:
            if not s_w in methods_in_s:
                methods_in_s.append(s_w)
        elif s_w in ['basting', 'pour', 'squeeze', 'seal', 'drain', 'discard', 'brush']:
            if not s_w in methods_in_s:
                methods_in_s.append(s_w)

    return methods_in_s

def get_time(s):
    time_in_s = []
    stop_words = ['about', 'for', ',']
    s = s.lower()
    unit = ''
    if 'minute' in s:
        unit = 'minute'
        end = s.index('minute')
    elif 'hour' in s:
        unit = 'hour'
        end = s.index('hour')
    else:
        return []

    s = s[:end]
    s = s.strip()
    words = s.split()
    for i in range(len(words)-1, -1 , -1):
        w = words[i]
        if w.isdigit():
            if int(w) > 1:
                unit = unit + 's'
            time_in_s.append(w)
            time_in_s.append(unit)
        elif w in stop_words:
            break
        if len(words)-1-i == 2:
            break

    return time_in_s

def print_directions(steps):

    for step in steps:
        print('Step {}'.format(step.step_number))
        print('Ingredients: {}'.format(step.ingredients))
        print('Tools: {}'.format(step.tools))
        print('Methods: {}'.format(step.methods))
        print('Times: {}'.format(step.time))

def main():
    recipe_data = load_recipe()
    steps = get_directions(recipe_data)
    print_directions(steps)

if __name__=='__main__':
    main()