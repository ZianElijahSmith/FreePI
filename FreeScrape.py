'''
FreeScrape.py

Copyright: Zian Elijah Smith
2023

Web Scrapper for FreePI
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
# used for scraping the HTTP data we receive from requests
try:
    from bs4 import BeautifulSoup
except(ImportError):
   raise ImportError("You need to install the python package bs4 (BeautifulSoup)")
   


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

# obviously all the lists we will use will be Free_liceneses
# However, we want to have a complete list so we know what to look for
# Additionally, it provides the user a complete list to view
Free_Licenses = [ Apache_Software_License_URL, Artistic_License_URL, GNU_Affero_General_Public_License_v3, GNU_Affero_General_Public_License_v3_or_later, GNU_Free_Documentation_License, GNU_General_Public_License, GNU_General_Public_License_v2, GNU_General_Public_License_v2_or_later, GNU_General_Public_License_v3, GNU_General_Public_License_v3_or_later, GNU_Lesser_General_Public_License_v2, GNU_Lesser_General_Public_License_v2_or_later, GNU_Lesser_General_Public_License_v3, GNU_Lesser_General_Public_License_v3_or_later, GNU_Library_or_Lesser_General_Public_License, MIT_License ]


# GPL Compatible lists, to help users find these specifically.
GPL_Compatible = [ Apache_Software_License_URL, Artistic_License_URL, GNU_Affero_General_Public_License_v3, GNU_Affero_General_Public_License_v3_or_later, GNU_Free_Documentation_License, GNU_General_Public_License, GNU_General_Public_License_v2, GNU_General_Public_License_v2_or_later, GNU_General_Public_License_v3, GNU_General_Public_License_v3_or_later, GNU_Lesser_General_Public_License_v2, GNU_Lesser_General_Public_License_v2_or_later, GNU_Lesser_General_Public_License_v3, GNU_Lesser_General_Public_License_v3_or_later, GNU_Library_or_Lesser_General_Public_License, MIT_License ]




def scan_packages(url):
    dictionary = {}
    
    # We're working with page 1 atm
    # This will be edited
    response = requests.get( url.format('1') )
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #get tags
    results = soup.select('li span')
    
    # step count is used for iterating in steps
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
        dictionary[step_count] = {'name':results[total_count].text, 'version':results[total_count+1].text, 'date':results[total_count+2].text}
        total_count += 3
        step_count += 1
    return dictionary


# example call
#scan_packages(GPLv2)



# returns the following data

'''
{0: {'name': 'fbadmin', 'version': '0.1.0.5', 'date': '\n  Jan 22, 2015\n'},
 1: {'name': 'bodhi-messages',
  'version': '7.1.1',
  'date': '\n  Mar 18, 2023\n'},
 2: {'name': 'bodhi-client', 'version': '7.1.1', 'date': '\n  Mar 18, 2023\n'},
 3: {'name': 'pymosaics', 'version': '0.2.0', 'date': '\n  Apr 14, 2020\n'},
 4: {'name': 'chessboard', 'version': '1.5.4', 'date': '\n  Aug 11, 2017\n'},
 5: {'name': 'pintail-asciidoc',
  'version': '0.3',
  'date': '\n  Jul 29, 2016\n'},
 6: {'name': 'DijkstraAlgo', 'version': '0.0.7', 'date': '\n  Feb 25, 2021\n'},
 7: {'name': 'edeposit.amqp.antivir',
  'version': '0.1-alpha',
  'date': '\n  Mar 12, 2014\n'},
 8: {'name': 'fedrq', 'version': '0.5.0', 'date': '\n  Mar 18, 2023\n'},
 9: {'name': 'packagedb-cli',
  'version': '2.14.1',
  'date': '\n  Jan 18, 2017\n'},
 10: {'name': 'roibuddy', 'version': '1.0.1', 'date': '\n  Sep 8, 2016\n'},
 11: {'name': 'pulp-cli-maven',
  'version': '0.2.0',
  'date': '\n  Mar 17, 2023\n'},
 12: {'name': 'pylogstash-context',
  'version': '0.1.19',
  'date': '\n  May 12, 2021\n'},
 13: {'name': 'column-print', 'version': '0.3.0', 'date': '\n  Mar 5, 2022\n'},
 14: {'name': 'hopla', 'version': '1.0.5', 'date': '\n  Jul 26, 2019\n'},
 15: {'name': 'uji', 'version': '0.2.1', 'date': '\n  Jan 7, 2020\n'},
 16: {'name': 'beaker-client',
  'version': '28.3',
  'date': '\n  May 21, 2022\n'},
 17: {'name': 'q-sdk', 'version': '0.0.1', 'date': '\n  Jul 21, 2021\n'},
 18: {'name': 'nitrate-tcms', 'version': '4.13', 'date': '\n  Nov 20, 2022\n'}}
'''





# In order to understand the code above, you need to understand this code below


'''
     ...: GPLv2_url = "https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+GNU+General+Public+License+v2+or+later+%28GPLv2%2B%29&o=&q=&page=
     ...: {}"
     ...: 
     ...: 
     ...: def get_packages(url):
     ...:     dictionary = {}
     ...: 
     ...:     # We're working with page 1 atm
     ...:     # This will be edited
     ...:     response = requests.get(url.format('1'))
     ...:     soup = BeautifulSoup(response.text, 'html.parser')
     ...: 
     ...:     #get tags
     ...:     results = soup.select('li span')
     ...: 
     ...:     count = 0
     ...:     # Gives us how many items there are
     ...:     length = len(results)
     ...: 
     ...:     while count < length:
     ...:         dictionary[count] = results[count].text
     ...:         count += 1
     ...:     return dictionary
     ...: 
     ...: 
     ...: 
     ...: get_packages(GPLv2_url)


'''



'''
output
     ...: get_packages(GPLv2_url)
Out[220]: 
{0: 'fbadmin',
 1: '0.1.0.5',
 2: '\n  Jan 22, 2015\n',
 3: 'bodhi-messages',
 4: '7.1.1',
 5: '\n  Mar 18, 2023\n',
 6: 'bodhi-client',
 7: '7.1.1',
 8: '\n  Mar 18, 2023\n',
 9: 'pymosaics',
 10: '0.2.0',
 11: '\n  Apr 14, 2020\n',
 12: 'chessboard',
 13: '1.5.4',
 14: '\n  Aug 11, 2017\n',
 15: 'pintail-asciidoc',
 16: '0.3',
 17: '\n  Jul 29, 2016\n',
 18: 'DijkstraAlgo',
 19: '0.0.7',
 20: '\n  Feb 25, 2021\n',
 21: 'edeposit.amqp.antivir',
 22: '0.1-alpha',
 23: '\n  Mar 12, 2014\n',
 24: 'fedrq',
 25: '0.5.0',
 26: '\n  Mar 18, 2023\n',
 27: 'packagedb-cli',
 28: '2.14.1',
 29: '\n  Jan 18, 2017\n',
 30: 'roibuddy',
 31: '1.0.1',
 32: '\n  Sep 8, 2016\n',
 33: 'pulp-cli-maven',
 34: '0.2.0',
 35: '\n  Mar 17, 2023\n',
 36: 'pylogstash-context',
 37: '0.1.19',
 38: '\n  May 12, 2021\n',
 39: 'column-print',
 40: '0.3.0',
 41: '\n  Mar 5, 2022\n',
 42: 'hopla',
 43: '1.0.5',
 44: '\n  Jul 26, 2019\n',
 45: 'uji',
 46: '0.2.1',
 47: '\n  Jan 7, 2020\n',
 48: 'beaker-client',
 49: '28.3',
 50: '\n  May 21, 2022\n',
 51: 'q-sdk',
 52: '0.0.1',
 53: '\n  Jul 21, 2021\n',
 54: 'nitrate-tcms',
 55: '4.13',
 56: '\n  Nov 20, 2022\n',
 57: 'house',
 58: '0.1.10',
 59: '\n  Jan 28, 2018\n'}



'''
