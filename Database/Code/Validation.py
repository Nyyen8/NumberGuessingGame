"""
Program: Validation.py
Author: Paul Elsea
Last Modified: 07/16/2020

Defining a variety of validation utility functions.
"""

from datetime import datetime as date
import re

'''Function to verify that input is valid name'''
def valid_name_check(input_string):
    result =  bool(re.fullmatch(r"^[^\W0-9_]+([ :'\-‧][^\W0-9_]+)*?$", input_string))
    return result


'''Function to verify that input is date'''
def valid_date(input_string):
    try:
        date.strptime(input_string, '%d-%m-%Y').date()
        return True
    except ValueError:
        return False


'''Function to verify that input uses only alphabetic characters'''
def valid_alpha_check(input_string):
    result = input_string.replace(" ", "").isalpha()
    return result