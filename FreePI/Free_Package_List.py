'''
It is planned to have 2 lists of the same data:
  1. A python dictionary from scraping PyPi
  2. A .json file, which will be made from the python dictionary
  
Allows us to have the freedom to work with either json or a python dictionary
'''

import json
    
# Not the full dictionary of all free packages
# will be replaced with full data later
Free_Packages_Dictionary = {0: {'name': 'fbadmin', 'version': '0.1.0.5', 'date': '\n  Jan 22, 2015\n'},
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

    
with open("Free_Packages.json", "w") as outfile:
    json.dump(dictionary, outfile)
