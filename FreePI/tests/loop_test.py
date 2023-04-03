# tested on Monday April 3rd 2023
# It works but needs testing to make sure it was 100% accurate

# ran on GPLv2 URL

try:
    import pydantic
except(ImportError):
    raise ImportError("You need to install the python package pydantic")

# requests is Apache-2.0 license
# used for making HTTP requests for webscraping
try:
    import requests
except(ImportError):
   raise ImportError("You need to install the python package requests")
   
# bs4 is MIT License (MIT)
# used for extracting the data we receive from scrapes via requests
try:
    from bs4 import BeautifulSoup
except(ImportError):
   raise ImportError("You need to install the python package bs4 (BeautifulSoup)")
   


dictionary = {}
dictionary_file = "/home/FreePI/dictionary.txt"


def get_max_pages(url: str) -> int:
    response = requests.get( url.format('1') )
    soup = BeautifulSoup(response.text, 'html.parser')
    # get page numbers
    buttons = soup.find_all('a', {'class': 'button-group__button'})
    #This should consistently give us the number of pages to loop through
    max_pages = int( buttons[ len(buttons) - 2 ].text )
    
    return max_pages
    
def parse_page(url: str, page=1) -> dict:

    response = requests.get( url.format(str(page)) )
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # get tags
    results = soup.select('li span')
    
    step_count = 0
    # total count takes into account EACH iteration
    total_count = 0
    
    # length = len(results) tells us how many items there are
    length = len(results)
    
    # since the items are divisible by three
    # name, version, date
    # this will tell us how many steps we need
    steps = length / 3
    
    # where the magic happens
    # .text is needed to extract the actual text FROM the html tags
    while total_count < (length-3):
        dictionary[step_count] = {'name':results[total_count].text, \
            'version':results[total_count+1].text, 'date':results[total_count+2].text}
        total_count += 3
        step_count += 1
        
    return dictionary




# type hints cheat sheet
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
def scan_packages(url: str, path_to_file: str) -> dict:
    global dictionary

    # might use a dictionary from a text file later

    
    # We're working with page 1 atm
    # This will be edited
    response = requests.get( url.format('1') )
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # get tags
    results = soup.select('li span')
    
    
    page = 1
    for each in range(0, (get_max_pages(url) + 2)):
        dictionary = ChainMap(dictionary, parse_page(url, page) )
        
        with open(dictionary_file, "a") as file_object:
            file_object.writelines( str( dictionary ) )
        page += 1
        
    return dictionary_file


# example call
scan_packages(GPLv2, dictionary_file)

# This gave us a dictionary of every package that was GPLv2 licensed
# New text file was 178.7 KB
