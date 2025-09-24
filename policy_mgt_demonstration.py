
### Policy Management System 
### Author: Kayode Ogunyemi
### Date: 23th September, 2025 


# Import Relevant Libraries 
from datetime import date



# create a POLICY HOLDER class
# ============================
class Policyholder:

    def __init__(self, holder_id, name, contact, product, start_date, end_date):
        # Policyholder details
        self.holder_id = holder_id
        self.name = name
        self.contact = contact
        self.status = "Pending"

        # Policy details (merged in)
        self.product = product
        self.policy_id = f"P-{holder_id}"
        self.start_date = start_date
        self.end_date = end_date
        self.policy_status = "Active"

        # Payments linked to this policyholder
        self.payments = []

    def register(self):
        if self.status == "Pending":
            self.status = "Active"
            print(f"Policyholder {self.name} registered with policy {self.policy_id}.")
        else:
            print(f"{self.name} is already {self.status}.")

    def suspend(self):
        self.policy_status = "Suspended"
        self.status = "Suspended"
        print(f"Policy {self.policy_id} for {self.name} has been suspended.")

    def reactivate(self):
        if self.policy_status == "Suspended":
            self.policy_status = "Active"
            self.status = "Active"
            print(f"Policy {self.policy_id} for {self.name} has been reactivated.")
        else:
            print(f"{self.name}'s policy is already active.")

    def add_payment(self, payment_id, amount, method="Bank Transfer"):
        payment = {
            "payment_id": payment_id,
            "amount": amount,
            "method": method,
            "date": date.today(),
            "status": "Completed"
        }
        self.payments.append(payment)
        print(f"Payment {payment_id} of {amount} recorded for {self.name}.")
        
        

    def display_account(self):
        print(f"Policyholder: {self.name} (ID: {self.holder_id})")
        print(f"Contact: {self.contact}")
        print(f"Status: {self.status}")
        print(f"Policy ID: {self.policy_id}, Product: {self.product}, Status: {self.policy_status}")
        for pay in self.payments:
            print(f"  Payment {pay['payment_id']}: {pay['amount']} via {pay['method']} on {pay['date']} [{pay['status']}]")
            
            
                 
       
            


# create a PAYMENT class
# ============================
class Payment:

    def __init__(self, payment_id, policy, amount, method="Bank Transfer"):
    
        self.payment_id = payment_id
        self.policy = policy
        self.amount = amount
        self.date = date.today()
        self.method = method
        self.status = "Completed"
        
        #Link Payment to Polcy 
        policy.payments.append(self)
        
        




# create a PRODUCT class
# ============================
class Product:


    def __init__(self, product_id, name, premium, coverage, status="Active"):
    
        #encapsulation of attributes using "__"
        self.product_id = product_id
        self.name = name
        self.premium = premium
        self.coverage = coverage
        self.status = status









#======================================
#DEMOSTRATION 
#======================================

# Create two policyholders (each with their policy included)
holder1 = Policyholder(1001, "KUNLE ORIYOMI", "08012345678", "LIFE Insurance", "2025-01-01", "2026-01-01")
holder2 = Policyholder(1002, "OLAWALE KENT", "08098765432", "CAR Insurance", "2025-02-01", "2026-02-01")
holder3 = Policyholder(1003, "GEORGE RAMAH", "08098110230", "HEALTH Insurance", "2025-07-01", "2026-02-01")



# Register 3 policy holders
print("\n")
print("List of Register PolicyHolders are listed below:")
print("================================================")
holder1.register()
holder2.register()
holder3.register()



# Add payments for each policy holders
print("\n")
print("Correspondin PolicyHolders Payments:")
print("================================================")
holder1.add_payment(4001, 50000, "Bank Transfer")
holder2.add_payment(4002, 75000, "Credit Card")
holder3.add_payment(4003, 70000, "Cash")


# Suspend and reactivate policyholders
print("\n")
print("Suspended and Reactivated Policy Holders:")
print("================================================")
holder1.suspend()
holder1.reactivate()


# Display details of Policy Holders
print("\n")
print("Policy Holders Full Details:")
print("================================================")
holder1.display_account()
holder2.display_account()
holder3.display_account()
