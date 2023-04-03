
# We need to generate something similar to https://pypi.org/simple/
# this file will eventually import our dictionary, and then generate such a file

def generate_repository(dictionary, file):
    total_count = len(dictionary)
    count = 0
    
    with open(file, "w") as file_object:
        for each in dictionary:
            file_object.writelines("<a href='/simple/{}'>{}</a>\n".format(
                d[count]['name'], d[count]["name"]))
            count += 1
    return file_object
