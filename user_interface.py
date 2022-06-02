"""
Writing a super basic user interface, we can make this better as we have time. 
"""




import transformers


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
    transformations = ['to vegetarian','from vegetarian','healthy','unhealthy','style-of-cuisine-placeholder']
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
    accept_url()
    #TODO Some transformations here 
    accept_transformation()