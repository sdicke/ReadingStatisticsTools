# ReadingStatisticsTools
Tools to summarise your reading progress


## bookpages.py

Calculates the mean and median of the pages of the books you read in a particular year.

### Requirements

* The script have be called with the `year` as command line argument
* * Example: python bookpages.py 2023
* The books are itemised in files on a per year base
* In the files there is one file per line
* The line format is name (`pages`) where `pages` are expressed by digits
* * Example: Buddenbrooks (904)
* The file names have to match the format `prefix` ++ `year` ++ `.md` where ++ is the concatenation operator
* * Example: /home/user/Documents/books_2023.md
* The prefix has to be specified in the script in the variable prefix in line 10. Please note that ~ will not replaced with your home directory path.
 be
