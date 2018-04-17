# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:56:07 2018

@author: krishna.i

Assignment 2.2: Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

starval= 5 # Initialization of starval variable to set max stars needed

if(starval > 0):        # check if Starval is greater than zero
    tempnum = 1         # taking tempnum varialble initialized with 1
    while tempnum <= starval :      #iterating till tempnum is less than or equal to starval
        i=1             # taking another variable to start iterating till starval value
        while i <=tempnum :     # Iterating from one star till starval is reached
            print("*",sep=' ',end=' ')
            i=i+1
        print("",end='\n')
        tempnum = tempnum + 1
    
    tempnum=tempnum - 2
    
    while tempnum >=1:
        j=tempnum
        while j >=1:             # Iterating from four stars till 1 star is printed
            print("*",sep=' ',end=' ')
            j=j-1
        print("",end='\n')
        tempnum=tempnum-1

