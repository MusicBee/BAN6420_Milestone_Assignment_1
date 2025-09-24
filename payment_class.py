
# Policy Management System - PAYMENT CLASS 
# Author: Kayode Ogunyemi
# Date: 23th September, 2025 



# Import Relevant Libraries 
from datetime import date




# Create a Payment Class
class Payment:

    def __init__(self, payment_id, policy, amount, method="Bank Transfer"):
    
        self.__payment_id = payment_id
        self.__policy = policy
        self.__amount = amount
        self.__date = date.today()
        self.__method = method
        self.status = "Completed"
        
        #Link Payment to Polcy 
        policy.payments.append(self)
        
        


