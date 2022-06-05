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

def get_directions(filename=None):
    recipe_data = load_recipe(filename)
    directions = recipe_data['directions']
    #Remove advertisement
    directions[0] = directions[0].replace('Advertisement', '')
    tools = get_tool_list()
    methods = parse_method(recipe_data)
    ingredients = recipe_data['ingredients']
    ingredients = ingredient_parser(ingredients)
    print(ingredients)
    #print(tools)
    #print(methods)

    '''"directions": ["    Step 1   Preheat oven to 375 degrees F (190 degrees C).    Advertisement ",
          "    Step 2   Season ground beef with garlic powder. Heat a large skillet over medium-high heat. Cook and stir ground beef in the hot skillet until browned and crumbly, 5 to 7 minutes. Drain and discard grease.   ",
          "    Step 3   Pour spaghetti sauce, tomato sauce, and oregano into a large saucepan. Set aside.   ",
          "    Step 4   Heat olive oil in a large skillet over medium-high heat. Saute garlic and onions until softened and translucent, about 5 minutes. Place cooked onion-garlic mixture and cooked ground beef into the sauce mixture. Cover and let simmer for 15 to 20 minutes.   ",
          "    Step 5   Combine mozzarella and provolone cheeses in a medium bowl. Mix ricotta cheese, eggs, milk, and 1/2 teaspoon oregano together in a separate bowl.   ",
          "    Step 6   Layer a 9x13-inch baking pan with just enough sauce to cover the bottom of the pan. Lay three lasagna noodles in the pan over the sauce. Cover with more sauce, then with ricotta mixture then sprinkle with mozzarella/provolone mixture; repeat layering. Finish with a layer of noodles and remaining sauce. Sprinkle top with Parmesan cheese.   ",
          "    Step 7   Bake, covered, in the preheated oven for 30 minutes. Uncover and continue to bake until cheese is melted and top is golden, about 15 minutes more.   "]'''

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
        step_ingredients = []
        step_tools = []
        step_methods = []
        step_times = []

        #start location after step n to substring:
        start = d.index(words[2])
        d = d[start:]
        sentences = split_into_sentences(d)
        for s in sentences:
            #print(step_number + '' + s)
            ingredients_in_s = get_ingredients(s, ingredients)
            #words = d.split()


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
        i = i.split(',')[0]
        if ')' in i:
            #To do: handle: "    4 (6 ounce) salmon steaks    ", it parses as 'steaks'
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
    return ingredients_in_s

def main():
    get_directions()

if __name__=='__main__':
    main()