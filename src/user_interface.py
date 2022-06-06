"""
Writing a super basic user interface, we can make this better as we have time. 
"""




import src.create_recipe as cr 
import src.dairy_free as df 
import src.half_double as scale
import src.health_transformer as ht

def accept_url():
    """
    Input: Nothing 

    Output: Returns a url from AllRecipes.com, or prints and error and prompts the user to try again if the url is not from AllRecipes
    #TODO add more checks to make sure real url 
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
    transformations = ['to vegetarian','from vegetarian','healthy','unhealthy','style-of-cuisine-placeholder','scale serving size', 'dairy free', 'just print recipe']
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



if __name__ == '__main__':
    url = accept_url()
    recipe = cr.create_recipe(url)
    transformation = accept_transformation()
    if transformation == 'to vegetarian':
        pass 
    elif transformation == 'from vegetarian':
        pass 
    elif transformation == 'healthy':
        transformed_recipe = ht.to_healthy(recipe)
    elif transformation == 'unhealthy':
        transformed_recipe = ht.to_unhealthy(recipe)
    elif transformation == 'style of cuisine placeholder':
        pass
    elif transformation == 'scale serving size':
        float_input = False
        while not float_input:
            scale_factor = input("By what factor would you like to scale this recipe?")
            try: 
                scale_factor = float(scale_factor)
                float_input = True 
                transformed_recipe = scale.scale_recipe(recipe,scale_factor)
            except:
                print("You did not enter a valid number to scale the recipe. Please try again. ")

    elif transformation == 'dairy free':
        transformed_recipe = df.dairy_free(recipe)
        
    elif transformation == 'just print recipe':
        pass

    #TODO Output somewhere here 