## At the moment, we have 2 main issues that need to be fixed as far as our code is concerned, 1 related to PyPi

### Code issues

### 1. Need to fix the indexing
FreePI starts indexing packages at 0 and it scans each page.
When FreePI goes from page 1 to page 2, it starts counting from 0 again.
This is giving us multiple dictionaries with values from 0 to approx 16-17.

One idea is change parse_page() and scan_packages() functions to make sure that FreePI counts from 0, and 
then adds each package based on total value, not page index.


### 2. Need to combine various dictionaries into 1 numerical dictionary
Self explanitory

### PyPi Issues

### 1. Package limit is 10,000
Suppose we go to https://pypi.org/search/ and we browse by license for the purposes of scanning all FOSS packages.
PyPi has a 10,000 package limit, which means if there are 14,000 packages under the Apache Software License,
our FreeScrape program will only be able to find 10,000 of them, not all 14,000.

Basically, PyPi stops generating pages after the 10,000th package (which I believe i 500 pages).

We've contacted PyPi, waited, and have received no response. That means we need to find an automated way to ensure we get all
packages under a FOSS license that takes the 10,000 package limit into account. It would be a pain to manually add them.

This issue has been the main holdup on the project.
