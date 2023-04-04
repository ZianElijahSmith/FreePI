
# We need to generate something similar to https://pypi.org/simple/
# this file will eventually import our dictionary, and then generate such a file



# give it a dictionary and an empty.html file
def generate_repository(dictionary, file):
    total_count = len(dictionary)
    count = 0
    # create a text file and write to it
    with open(file, "t+w") as file_object:
        file_object.writelines("<!DOCTYPE html> \n")
        file_object.writelines("<html> \n")
        file_object.writelines("<head> \n")
        file_object.writelines("</head> \n")
        file_object.writelines("<body> \n")

        for each in dictionary:
            # originally were gonna host our own files but
            # we can just refer to pypi
            file_object.writelines("<a href='https://pypi.org/simple/{}'>{}</a> \n".format(
                d[count]['name'], d[count]["name"]))
            count += 1

        file_object.writelines("</body> \n")
        file_object.writelines("</html>")
    return file_object


'''
This function was given the following dictionary:

d = {0: {'name': 'fbadmin', 'version': '0.1.0.5', 'date': '\n  Jan 22, 2015\n'},
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

# Generates a file that will contain the following output
# generate_repository(d, '/home/gnunix/FreePI/FreePI/test.html')
'''
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<a href='https://pypi.org/simple/fbadmin'>fbadmin</a>
<a href='https://pypi.org/simple/bodhi-messages'>bodhi-messages</a>
<a href='https://pypi.org/simple/bodhi-client'>bodhi-client</a>
<a href='https://pypi.org/simple/pymosaics'>pymosaics</a>
<a href='https://pypi.org/simple/chessboard'>chessboard</a>
<a href='https://pypi.org/simple/pintail-asciidoc'>pintail-asciidoc</a>
<a href='https://pypi.org/simple/DijkstraAlgo'>DijkstraAlgo</a>
<a href='https://pypi.org/simple/edeposit.amqp.antivir'>edeposit.amqp.antivir</a>
<a href='https://pypi.org/simple/fedrq'>fedrq</a>
<a href='https://pypi.org/simple/packagedb-cli'>packagedb-cli</a>
<a href='https://pypi.org/simple/roibuddy'>roibuddy</a>
<a href='https://pypi.org/simple/pulp-cli-maven'>pulp-cli-maven</a>
<a href='https://pypi.org/simple/pylogstash-context'>pylogstash-context</a>
<a href='https://pypi.org/simple/column-print'>column-print</a>
<a href='https://pypi.org/simple/hopla'>hopla</a>
<a href='https://pypi.org/simple/uji'>uji</a>
<a href='https://pypi.org/simple/beaker-client'>beaker-client</a>
<a href='https://pypi.org/simple/q-sdk'>q-sdk</a>
<a href='https://pypi.org/simple/nitrate-tcms'>nitrate-tcms</a>
</body>
</html>

'''
