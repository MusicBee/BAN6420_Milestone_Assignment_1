
# Policy Management System - POLICYHOLDER CLASS 
# Author: Kayode Ogunyemi
# Date: 23th September, 2025 


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



    #Register New Holder
    def register(self):
        if self.status == "Pending":
            self.status = "Active"
            print(f"Policyholder {self.name} registered with policy {self.policy_id}.")
        else:
            print(f"{self.name} is already {self.status}.")

    #Suspend Existing Holder
    def suspend(self):
        self.policy_status = "Suspended"
        self.status = "Suspended"
        print(f"Policy {self.policy_id} for {self.name} has been suspended.")

    #Reactiveate Holders 
    def reactivate(self):
        if self.policy_status == "Suspended":
            self.policy_status = "Active"
            self.status = "Active"
            print(f"Policy {self.policy_id} for {self.name} has been reactivated.")
        else:
            print(f"{self.name}'s policy is already active.")


    #Add payment
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
        
        
    #View Policyholders
    def display_account(self):
        print(f"\nPolicyholder: {self.name} (ID: {self.holder_id})")
        print(f"Contact: {self.contact}")
        print(f"Status: {self.status}")
        print(f"Policy ID: {self.policy_id}, Product: {self.product}, Status: {self.policy_status}")
        for pay in self.payments:
            print(f"  Payment {pay['payment_id']}: {pay['amount']} via {pay['method']} on {pay['date']} [{pay['status']}]")


