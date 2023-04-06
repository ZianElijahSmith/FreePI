import json

path_to_json = '/home/gnunix/FreePI/FreePI/tests/test.json'
path_to_dictionary = '/home/gnunix/FreePI/FreePI/tests/test_dictionary.py'

def json_to_dictionary(path_to_file):
    with open(path_to_file) as json_file:
        data = json.load(json_file)
    return data
