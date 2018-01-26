# ccode_replace_python
python translation of Clayton Thyne's replace_ccode_country.do stata file
#########################################################################################
This script allows python users to utilize Clayton Thyne's Stata file for creating ccodes
in country-level datasets. Allows for easy merging.
##################################################################################
#use clthyn.txt file for strings of stata code
#file_name is clthyn.txt, df is whichever df you use
#scrapes ccodes and country names in order and 
#creates a ccode variable in the dataset based on country names. 
#credit for ccode/country information goes to Dr. Clayton Thyne at Kentucky
#based on original .do file made by Thyne
#see http://www.uky.edu/~clthyn2/research.htm for more.
#    
#example use
from replace_ccode_country import ccode_make
df = ccode_make(df, 'clthyn.txt', 'country')

###################################################
#adds ccode to your dataset
ccode_make(df, file_name, c_var)
#df = your data frame
#file_name = clayton thyne's do script in modified text form
#c_var = the original country string variable name from your df
##########################################################################################
