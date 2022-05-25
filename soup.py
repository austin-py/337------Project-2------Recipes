from bs4 import BeautifulSoup
import requests


def get_soup(url):
    """
    Input: Takes a url content  

    Output: Returns the BeautifulSoup object of the html it recieved, parsed. 
    """
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    return soup 


if __name__ == '__main__':
    soup = get_soup(' https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/')
    print(soup.text)