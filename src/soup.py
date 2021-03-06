from bs4 import BeautifulSoup
import requests
import json
import os


def get_soup(url):
    """
    Input: Takes a url content  

    Output: Returns the BeautifulSoup object of the html it recieved, parsed. 
    """
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    return soup 

def get_ingredients(soup):
    """
    Input: Takes a soup object from BS4

    Output: Returns a list of ingredients
    """
    mydivs = soup.find_all("li", "ingredients-item")
    ingredients = []
    for elem in mydivs:
        ingredients.append(elem.text)
    return ingredients

def get_directions(soup):
    """
    Input: Takes a soup object from BS4

    Output: Returns a list of cooking directions
    """
    mydivs = soup.find_all("li", "subcontainer instructions-section-item")
    directions = []
    for elem in mydivs:
        directions.append(elem.text)
    return directions   

def get_nutrition_facts(soup):
    """
    Input: Takes a soup object from BS4

    Output: Returns a string of nutrition facts
    """
    elem = soup.find("div", "recipe-nutrition-section")
    return elem.text

def get_general_info(soup):
    """
    Input: Takes a soup object from BS4

    Output: Returns a list of general info about the recipe 
    """
    mydivs = soup.find_all("div", "recipe-meta-item")
    general_info = []
    for elem in mydivs:
        general_info.append(elem.text)
    return general_info   

def dump_info_to_txt(url):
    """
    Input: Takes a url from AllRecipes.com

    Output: Returns nothing, but creates a txt file with the recipe info. 
    """
    soup = get_soup(url)
    ingredients = get_ingredients(soup)
    directions = get_directions(soup)
    nutrition_facts = get_nutrition_facts(soup)
    general_info = get_general_info(soup)

    with open(os.getcwd()+'/../Data/recipe_data.txt','w') as f:
        f.write('Recipe Name: {}\n\n\n'.format(url_to_name(url)))
        f.write("Ingredients:\n")
        for ingredient in ingredients:
            f.write("   -{}\n".format(ingredient))

        f.write("\n\n\n")

        f.write("Directions:\n")
        for direction in directions: 
            f.write("   -{}\n".format(direction))

        f.write("\n\n\n")

        f.write("Nutrition Facts: {}\n".format(nutrition_facts))

        f.write("\n\n\n")
 
        f.write("General Info:\n")
        for info in general_info: 
            f.write("   -{}\n".format(info))

def dump_info_to_json(url):
    """
    Input: Takes a url from AllRecipes.com

    Output: Returns nothing but creates a json file with the recipe info
    """
    soup = get_soup(url)

    dict_to_dump = {
         'Recipe Name' : url_to_name(url), 
         "ingredients": get_ingredients(soup),
         "directions" : get_directions(soup),
         "nutrition_facts" : get_nutrition_facts(soup),
         "general_info" : get_general_info(soup)
         }
    with open(os.getcwd()+'/../Data/recipe_data.json','w') as f:
        json.dump(dict_to_dump,f,indent=5)

def get_soup_dictionary(url):
    """
    Input: Takes url from AllRecipes.com

    Output: Returns a dictionary of the recipe info 
    """
    soup = get_soup(url)
    dict_to_dump = {
     "ingredients": get_ingredients(soup),
     "directions" : get_directions(soup),
     "nutrition_facts" : get_nutrition_facts(soup),
     "general_info" : get_general_info(soup)
    }
    return dict_to_dump

def get_soup_dictionary_w_soup(soup):
    """
    Input: Takes a soup object from BS4

    Output: Returns a dictionary of the recipe info 
    """
    dict_to_dump = {
     "ingredients": get_ingredients(soup),
     "directions" : get_directions(soup),
     "nutrition_facts" : get_nutrition_facts(soup),
     "general_info" : get_general_info(soup)
    }
    return dict_to_dump

def url_to_output(url):
    """
    Input: Takes a url from allrecipes.com

    Output: Returns a dictionary of recipe data & creates a json and text output file. 
    """
    dump_info_to_txt(url)
    dump_info_to_json(url)
    dict = get_soup_dictionary(url)
    return dict 

def url_to_name(url):
    """
    Input: Takes a url from allrecipes.com

    Output: Returns a string that is the name of the recipe (from the url).
    """
    split_url = url.split("/")
    recipe_name = split_url[-2]
    recipe_name = recipe_name.split('-')
    name = " ".join(recipe_name)
    return name

if __name__ == '__main__':
    url_to_output(' https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/')
    #url_to_output('https://www.allrecipes.com/recipe/244716/shirataki-meatless-meat-pad-thai/')