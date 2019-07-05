# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:33:40 2019

@author: DELL PC
"""

def song():
    print("Old town road" )
song()


def artist():
    print("Lil Nas X")    # using print action inside the funtion 
artist()    # when we call this funtion the result of the  attribute is shown in the output
    


def year():
    print("2019")
year()    


# below there is a example for boolean

one = []
print(one,'is',bool(one))

two = [0]
print(two,'is',bool(two))

three = 0.0
print(three,'is',bool(three))

four = None
print(four,'is',bool(four))

five = True
print(five,'is',bool(five))

six = 'Easy string'
print(six,'is',bool(six))