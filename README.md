# ccode_replace_python
# Python translation of Clayton Thyne's replace_ccode_country.do stata file


This script allows python users to utilize Clayton Thyne's Stata file for creating ccodes in country-level datasets. Allows for easy merging. Uses a modified text file of original stata code to scrape ccode numbers and country name strings. 


# Credit for ccode/country information goes to Dr. Clayton Thyne at Kentucky. Process based on original .do file made by Thyne. See http://www.uky.edu/~clthyn2/research.htm for more information.


# Example code

```
from replace_ccode_country import ccode_make

df = ccode_make(df, 'clthyn.txt', 'country')


```
# Argument key

ccode_make(df, file_name, c_var)

1. df = your data frame
2. file_name = clayton thyne's do script in modified text form
3. c_var = the original country string variable name from your df

