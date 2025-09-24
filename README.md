# Policy Management System (Prototype)

Nexford Assignment for BAN6420. A **Policy Management System** prototype implemented in Python.  
It demonstrates the use of Object-Oriented Programming (OOP) concepts to model an insurance system that manages **policyholders, products, and payments**.

---

## Features

- **Policyholder Management**
  - Register new policyholders
  - Suspend and reactivate policyholders
  - Each policyholder can own a policy (with product details included)

- **Product**
  - Products are linked to policyholders when they register

- **Payments**
  - Record payments made by policyholders
  - Track payment method, date, and status

- **Account Management**
  - Display complete account details for each policyholder
  - Show policy and payment history

---

## Project Structure

- `Policyholder` class (combined with Policy details)
  - Manages policyholder registration, suspension, reactivation
  - Stores policy information (ID, product, start/end date, status)
  - Stores payments linked to the policyholder

---

## Example Usage

```python
# Create two policyholders (each with their policy included)
holder1 = Policyholder(1001, "John Doe", "08012345678", "Life Insurance", "2025-01-01", "2026-01-01")
holder2 = Policyholder(1002, "Jane Smith", "08098765432", "Health Insurance", "2025-02-01", "2026-02-01")

# Register them
holder1.register()
holder2.register()

# Add payments
holder1.add_payment(4001, 50000, "Bank Transfer")
holder2.add_payment(4002, 75000, "Credit Card")

# Suspend and reactivate
holder1.suspend()
holder1.reactivate()

# Display details
holder1.display_account()
holder2.display_account()
```

---

## Sample Output

List of Register PolicyHolders are listed below:
================================================
Policyholder KUNLE ORIYOMI registered with policy P-1001.
Policyholder OLAWALE KENT registered with policy P-1002.
Policyholder GEORGE RAMAH registered with policy P-1003.


Correspondin PolicyHolders Payments:
================================================
Payment 4001 of 50000 recorded for KUNLE ORIYOMI.
Payment 4002 of 75000 recorded for OLAWALE KENT.
Payment 4003 of 70000 recorded for GEORGE RAMAH.


Suspended and Reactivated Policy Holders:
================================================
Policy P-1001 for KUNLE ORIYOMI has been suspended.
Policy P-1001 for KUNLE ORIYOMI has been reactivated.


Policy Holders Full Details:
================================================
Policyholder: KUNLE ORIYOMI (ID: 1001)
Contact: 08012345678
Status: Active
Policy ID: P-1001, Product: LIFE Insurance, Status: Active
  Payment 4001: 50000 via Bank Transfer on 2025-09-24 [Completed]
Policyholder: OLAWALE KENT (ID: 1002)
Contact: 08098765432
Status: Active
Policy ID: P-1002, Product: CAR Insurance, Status: Active
  Payment 4002: 75000 via Credit Card on 2025-09-24 [Completed]
Policyholder: GEORGE RAMAH (ID: 1003)
Contact: 08098110230
Status: Active
Policy ID: P-1003, Product: HEALTH Insurance, Status: Active
  Payment 4003: 70000 via Cash on 2025-09-24 [Completed]



---

## Notes

- This is a **prototype** for learning OOP in Python.  
- In real-world systems, policyholders may own **multiple policies**.  
- A database (e.g., PostgreSQL, MySQL) and API framework (e.g., Django, FastAPI) would be required for production.



## Author

- **Kayode Ogunyemi**
- **Date: 24th September, 2025**
