
# Policy Management System - PRODUCT CLASS 
# Author: Kayode Ogunyemi
# Date: 23th September, 2025 


# Import Relevant Libraries 
from datetime import date



# Create a Poduct Class
class Product:


    def __init__(self, product_id, name, premium, coverage, status="Active"):
    
        #encapsulation of attributes using "__"
        self.__product_id = product_id
        self.__name = name
        self.__premium = premium
        self.__coverage = coverage
        self.__status = status




