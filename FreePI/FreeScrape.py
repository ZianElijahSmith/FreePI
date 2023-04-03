# tested on Monday April 3rd 2023
# It works but needs testing to make sure it was 100% accurate

# ran on GPLv2 URL


'''
FreeScrape.py

Copyright: Zian Elijah Smith
2023

Web Scrapper for FreePI

FreeScrape conducts webscraping on PyPi and collects the Free Software packages.
Searches are conducted by cheacking each license page.

This file is still being developed.
License: GPL-3.0 license
'''

# Pydantic is MIT license
# Used for providing documentation and annotations to variables, etc
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

# collections is Apache License 2.0
# Also in standard library
# ChainMap is used to combine dictionaries in their respective order
from collections import ChainMap
   
   
   
# Licenses, in alphabetical order

#1
# Apache variable url
# The {} at the end will be replaced with whatever page you want
Apache_Software_License_URL = ASL =  "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+Apache+Software+License&c=Programming+Language+%3A%3A+Python&o=&q=&page={}"

#2
# Artistic License
Artistic_License_URL = AL = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+Artistic+License&o=&q=&page={}"

#3
# GPLv2 variable url
# The {} at the end will be replaced with whatever page you want
GNU_Affero_General_Public_License_v3 = AGPLv3 = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Affero+General+Public+License+v3&o=&q=&page={}"

#4
GNU_Affero_General_Public_License_v3_or_later = AGPLv3plus = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Affero+General+Public+License+v3+or+later+%28AGPLv3%2B%29&o=&q=&page={}"

#5
GNU_Free_Documentation_License = FDL = GFDL = "https://pypi.org/search/?q=&o=&c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Free+Documentation+License+%28FDL%29&o=&q=&page={}"

#6
GNU_General_Public_License = GPL = "https://pypi.org/search/?q=&o=&c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+General+Public+License+%28GPL%29&o=&q=&page={}"

#7
GNU_General_Public_License_v2 = GPLv2 = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+General+Public+License+v2+%28GPLv2%29&o=&q=&page={}"

#8
GNU_General_Public_License_v2_or_later = GPLv2plus = "https://pypi.org/search/?q=&o=&c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+General+Public+License+v2+or+later+%28GPLv2%2B%29&o=&q=&page={}"

#9
GNU_General_Public_License_v3 = GPLv3 = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+General+Public+License+v3+%28GPLv3%29&o=&q=&page={}"

#10
GNU_General_Public_License_v3_or_later = GPLv3plus = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+General+Public+License+v3+or+later+%28GPLv3%2B%29&o=&q=&page={}"

#11
GNU_Lesser_General_Public_License_v2 = LGPLv2 = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Lesser+General+Public+License+v2+%28LGPLv2%29&o=&q=&page={}"

#12
GNU_Lesser_General_Public_License_v2_or_later = LGPLv2plus = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Lesser+General+Public+License+v2+or+later+%28LGPLv2%2B%29&o=&q=&page={}"

#13
GNU_Lesser_General_Public_License_v3 = LGPLv3 = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Lesser+General+Public+License+v3+%28LGPLv3%29&o=&q=&page={}"

#14
GNU_Lesser_General_Public_License_v3_or_later = LGPLv3plus = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Lesser+General+Public+License+v3+or+later+%28LGPLv3%2B%29&o=&q=&page={}"

#15
GNU_Library_or_Lesser_General_Public_License = LGPL = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+Library+or+Lesser+General+Public+License+%28LGPL%29&o=&q=&page={}"

#16
MIT_License = MIT = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License&o=&q=&page={}"

#17
Python_Software_Foundation_License = PSF = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+Python+Software+Foundation+License&o=&q=&page={}"

# obviously all the lists we will use will be Free_liceneses
# However, we want to have a complete list so we know what to look for
# Additionally, it provides the user a complete list to view

# https://www.gnu.org/licenses/license-list.en.html
Free_Licenses = [ Apache_Software_License_URL, Artistic_License_URL, \
GNU_Affero_General_Public_License_v3, GNU_Affero_General_Public_License_v3_or_later, \
GNU_Free_Documentation_License, GNU_General_Public_License, GNU_General_Public_License_v2, \
GNU_General_Public_License_v2_or_later, GNU_General_Public_License_v3, \
GNU_General_Public_License_v3_or_later, GNU_Lesser_General_Public_License_v2, \
GNU_Lesser_General_Public_License_v2_or_later, GNU_Lesser_General_Public_License_v3, \
GNU_Lesser_General_Public_License_v3_or_later, GNU_Library_or_Lesser_General_Public_License, \
MIT_License, Python_Software_Foundation_License ]


# GPL Compatible lists, to help users find these specifically.

# https://www.gnu.org/licenses/license-list.en.html#GPLCompatibleLicenses
GPL_Compatible = [ Apache_Software_License_URL, Artistic_License_URL, \
GNU_Affero_General_Public_License_v3, GNU_Affero_General_Public_License_v3_or_later, \
GNU_Free_Documentation_License, GNU_General_Public_License, GNU_General_Public_License_v2, \
GNU_General_Public_License_v2_or_later, GNU_General_Public_License_v3, \
GNU_General_Public_License_v3_or_later, GNU_Lesser_General_Public_License_v2, \
GNU_Lesser_General_Public_License_v2_or_later, GNU_Lesser_General_Public_License_v3, \
GNU_Lesser_General_Public_License_v3_or_later, GNU_Library_or_Lesser_General_Public_License ]
   


dictionary = {}
# this will need to be edited
dictionary_file = "/home/gnunix/FreePI/dictionary.txt"


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



def scan_packages(url: str, path_to_file: str) -> dict:
    global dictionary

    # might use a dictionary from a text file later

    
    response = requests.get( url.format('1') )
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # get tags
    results = soup.select('li span')
    
    
    page = 1
    with open(dictionary_file, "a") as file_object:
        for each in range(1, (get_max_pages(url) + 1)):
            file_object.writelines( str( parse_page(url, page) ) )
            page += 1
        
    return


# example call
scan_packages(GPLv2, dictionary_file)

# previous version was giving us each package 4 times
# this has been fixed

# dictionary file size with example call was 175.9 kB
