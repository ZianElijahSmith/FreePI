dictionary = {}

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
def scan_packages(url: str) -> dict:
    global dictionary

    # might use a dictionary from a text file later

    
    # We're working with page 1 atm
    # This will be edited
    response = requests.get( url.format('1') )
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # get tags
    results = soup.select('li span')
    
    
    page = 1
    for each in range(0, (get_max_pages(url) + 1)):
        dictionary = ChainMap(dictionary, parse_page(url,) )
        page += 1
    return dictionary


# example call
scan_packages(GPLv2)
