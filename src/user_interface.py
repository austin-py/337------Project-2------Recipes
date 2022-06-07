import copy 
import create_recipe as cr 
import dairy_free as df 
import half_double as scale
import health_transformer as ht
import vegetarian as ve
import asian_transformer as at 
#TODO import jaheels code here when he pushes it 

def accept_url():
    """
    Input: Nothing 

    Output: Returns a url from AllRecipes.com, or prints and error and prompts the user to try again if the url is not from AllRecipes
    """
    while True:
        url = input("Please input a url from AllRecipes.com: \n\n")
        split_url = url.split("/")
        if split_url[2] != 'www.allrecipes.com':
            print("I'm sorry, you input a url that is not from allrecipes.com, please try again!\n\n")
        else:
            return(url)

def accept_transformation():
    """
    Input: Nothing 
    
    Output: Returns the user-selected transformation from the available list
    #TODO add the style of cuisine we are doing to transformation list 
    """
    transformations = ['to vegetarian','from vegetarian','healthy','unhealthy','asian','scale serving size', 'dairy free', 'just print recipe']
    while True:
        print("Please choose a transformation from the following options:")
        for i in transformations:
            print("     -{}".format(i))
        print()

        transformation = input()
        if transformation not in transformations:
            print("I'm sorry, you input a transformation that is not on the available list. Please try again!\n\n")
        else:
            return(transformation)

def main():
    url = accept_url()
    recipe = cr.create_recipe(url)

    transformation = accept_transformation()
    recipe_to_transform = copy.deepcopy(recipe)

    if transformation == 'to vegetarian':
        transformed_recipe, change = ve.to_vegetarian(recipe_to_transform)
        print(change)
    elif transformation == 'from vegetarian':
        transformed_recipe, change = ve.to_non_vegetarian(recipe_to_transform)
        print(change)
    elif transformation == 'healthy':
        transformed_recipe = ht.to_healthy(recipe_to_transform)
    elif transformation == 'unhealthy':
        transformed_recipe = ht.to_unhealthy(recipe_to_transform)
    elif transformation == 'asian':
        transformed_recipe= at.asianized(recipe_to_transform)
    elif transformation == 'scale serving size':
        float_input = False
        while not float_input:
            scale_factor = input("By what factor would you like to scale this recipe?\n")
            try: 
                scale_factor = float(scale_factor)
                float_input = True 
                transformed_recipe = scale.scale_recipe(recipe_to_transform,scale_factor)
            except:
                print("You did not enter a valid number to scale the recipe. Please try again. ")

    elif transformation == 'dairy free':
        transformed_recipe = df.dairy_free(recipe_to_transform)
        
    elif transformation == 'just print recipe':
        recipe.print_recipe()
        return

    print("The recipe before transformation was:")
    recipe.print_recipe()
    print('\n\n\n')
    print('The recipe after transformation was:')
    transformed_recipe.print_recipe()

if __name__ == '__main__':
    while True:
        main()