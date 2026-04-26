transactions = []

def add_transaction():
    date = input("Enter date: ")
    amount = float(input("Enter amount: "))
    merchant = input("Enter merchant: ").strip().lower()

    transaction = {
        "date": date,
        "amount": amount,
        "merchant": merchant
    }

    transactions.append(transaction)
    print("Transaction added!")

def view_transactions():
    print("\nAll Transactions")
    for t in transactions:
        print(t)

def search_merchant():
    name = input("Enter merchant to search: ").lower()

    for t in transactions:
        if name in t["merchant"]:
            print(t)

while True:
    print("\n1 Add Transaction")
    print("2 View Transactions")
    print("3 Search Merchant")
    print("4 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_transaction()

    elif ch == "2":
        view_transactions()

    elif ch == "3":
        search_merchant()

    elif ch == "4":
        break