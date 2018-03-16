# -*- coding: utf-8 -*-
"""
Clayton Thyne CCODE DOFILE 
Translated to Python
Created on Fri Jan 26 11:44:25 2018

@author: OEFDataScience
"""

#packages
import numpy as np
import re

#functions

def clthyn_scrape(file_name):
    #extract ccode numbers in order
    cnums = []
    #read text file and store in var
    with open (file_name, 'rt') as in_file:
        for line in in_file:
           match = re.search('\d+', line)
           if match:
               cnums.append(int(match.group()))
    #convert 999s to -999s
    cnums = np.where(np.asarray(cnums)==999, -999, np.asarray(cnums))
    #extract country names in order
    cnames = []
    #read text file and store in var
    with open (file_name, 'rt') as in_file:
        for line in in_file:
            match = re.search('"([^"]*)"', line)
            if match:
                cnames.append(str(match.group()))

    for i in range(len(cnames)):
        cnames[i] = cnames[i].replace('"', '')
          
    return cnums, cnames


def ccode_make(df, file_name, c_var):
    
    ccodes, country_names = clthyn_scrape(file_name)
    
    df['ccode'] = np.nan
    
    for i, n in zip(ccodes, country_names):
        df['ccode'] = np.where(df[c_var]==n,
          i, df['ccode'])
        
    return df

def ccode_name(df, file_name, c_var):
    
    country_names, ccodes = clthyn_scrape(file_name)
    
    df['country_names'] = np.nan
    
    for i, n in zip(ccodes, country_names):
        df['country_names'] = np.where(df[c_var]==n, 
          i, df['country_names'])
    
    return df
    
##################################################################################
#use clthyn.txt file for strings of stata code
#file_name is clthyn.txt, df is whichever df you use
#scrapes ccodes and country names in order and 
#creates a ccode variable in the dataset based on country names. 
#original .do file made by Dr. Thyne at Kentucky
#see http://www.uky.edu/~clthyn2/research.htm for more.
#    
#example use
#from replace_ccode_country import ccode_make
#    
#df = ccode_make(df, 'clthyn.txt', 'country')
#   
#adds ccode to your dataset
#df = your data frame
#file_name = clayton thyne's do script in text form
#c_var = the original country variable name from df
##########################################################################################
    
