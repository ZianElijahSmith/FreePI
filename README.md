# FreePI

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
