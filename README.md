# FreePI (Still being developed)

## FreePI is the Free Package Index, a version of PyPi that includes ONLY 100% Free Software ("Free" as in "Free speech" not "Free beer")
https://freepi.org/

Founded April 1st 2023 by ahoka (no, not an April fools joke)
**In Development**

## Important note!!
PyPi has a package index limit on their search pages (based on license) of 10,000 packages, even though some licenses indexes have more than 10,000 packages.

Since FreePI is scanning PyPi for packages, this means FreePI won't be able to get all packages that fit a license.
This issue comes from PyPi's 10,000 limit and is not an issue with FreePI, but it will hinder and slow down FreePI's development.

We are contacting PyPi and thinking of a solution to this issue.

## Welcome to FreePI
<br />
FreePI (pronounced "Free Pie") is a Python package index that only includes and proposes <a href="https://www.gnu.org/philosophy/free-sw.html">free software</a>. We reject nonfree software and documentation. If we discover that any nonfree software or documentation has been included by mistake, it will be removed.

To learn more about "Free Software", please watch this 13 minute~ TEDTalk by Richard Stallman.
https://www.youtube.com/watch?v=Ag1AKIl_2GM

## How FreePI Works
<br />
FreePI works just like any other package index, but with the added benefit of only including free software. You can use the pip package manager to install packages using FreePi, just as you would with PyPI or any other index.

## Get Started with FreePI
<br />
Getting started with FreePI is easy. Once it's completed, just add the FreePI index to your pip configuration by running the following command:
<pre>pip config set global.index-url https://freepi.org/simple/</pre>

Once you've added the FreePI index to your pip configuration, you can use the pip install command to install packages from FreePI, just as you would with PyPI:
<pre>pip install package-name</pre>

## Contact Us
If you have any questions, feedback about FreePI or if you would like to contribute, please visit the channel #freepi on irc.libera.chat.

Developed by ahoka and jxself. (jxself is a FSF member)
(ahoka, aka Zian, gives special thanks to jsxself for helping with this project on day one)

You can find jxself's website here:
https://jxself.org/

## Update
Our original intent was for FreePI to be a free software only version of PyPi. However, there are plans to begin the process of listing nothing but free software for other programming languages and their respective packages, such as RubyGems for Ruby, once our filtering of PyPi is complete.

Thus, FreePI will be The Free Package Index.



## Issues: at the moment, we have 2 main issues that need to be fixed as far as our code is concerned, 1 related to PyPi

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
