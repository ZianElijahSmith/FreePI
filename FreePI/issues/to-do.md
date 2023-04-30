At the moment, we have 2 main issues that need to be fixed.

## 1. Need to fix the indexing
FreePI starts indexing packages at 0 and it scans each page.
When FreePI goes from page 1 to page 2, it starts counting from 0 again.
This is giving us multiple dictionaries with values from 0 to approx 16-17.

What we need to do is change parse_page() and scan_packages() functions to make sure that FreePI counts from 0, and 
then adds each package based on total value, not page index.



## 2. Need to combine various dictionaries into 1 numerical dictionary
Self explanitory



Will try to make 1 commit and fix per weeekend, been busy past 2 weeks.
