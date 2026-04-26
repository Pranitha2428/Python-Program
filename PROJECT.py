# week1_basic_transaction.py
print("Smart Finance Manager")

date = input("Enter transaction date: ")
amount = float(input("Enter amount: "))
t_type = input("Enter type (Credit/Debit): ")
merchant = input("Enter merchant name: ")
notes = input("Enter notes: ")

if amount <= 0:
    print("Invalid amount")
else:
    print("\nTransaction Summary")
    print(f"Date: {date}")
    print(f"Amount: ₹{amount}")
    print(f"Type: {t_type}")
    print(f"Merchant: {merchant}")
    print(f"Notes: {notes}")