
# We need to generate something similar to https://pypi.org/simple/
# this file will eventually import our dictionary, and then generate such a file

# give it a dictionary and an empty.html file
def generate_repository(dictionary, file):
    total_count = len(dictionary)
    count = 0
    
    with open(file, "w") as file_object:
        for each in dictionary:
            file_object.writelines("<a href='/simple/{}'>{}</a>\n".format(
                d[count]['name'], d[count]["name"]))
            count += 1
    return file_object

# Generates a file that will contain the following output
'''
<a href='/simple/packagedb-cli'>packagedb-cli</a>
<a href='/simple/roibuddy'>roibuddy</a>
<a href='/simple/pulp-cli-maven'>pulp-cli-maven</a>
<a href='/simple/pylogstash-context'>pylogstash-context</a>
<a href='/simple/column-print'>column-print</a>
<a href='/simple/hopla'>hopla</a>
<a href='/simple/uji'>uji</a>
<a href='/simple/beaker-client'>beaker-client</a>
<a href='/simple/q-sdk'>q-sdk</a>
<a href='/simple/nitrate-tcms'>nitrate-tcms</a>
'''
