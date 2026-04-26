transactions = []

def validate_amount(amount):
    return amount > 0

def classify_transaction(merchant):
    merchant = merchant.lower()

    if "swiggy" in merchant or "zomato" in merchant:
        return "Food"
    elif "uber" in merchant or "ola" in merchant:
        return "Transport"
    else:
        return "Others"

def add_transaction():
    date = input("Enter date: ")
    amount = float(input("Enter amount: "))

    if not validate_amount(amount):
        print("Invalid amount")
        return

    merchant = input("Enter merchant: ")

    category = classify_transaction(merchant)

    transaction = {
        "date": date,
        "amount": amount,
        "merchant": merchant,
        "category": category
    }

    transactions.append(transaction)
    print("Transaction added!")

def display_transactions():
    for t in transactions:
        print(t)

def search_transactions():
    merchant = input("Enter merchant name: ")

    for t in transactions:
        if merchant.lower() in t["merchant"].lower():
            print(t)

while True:
    print("\n1 Add Transaction")
    print("2 View Transactions")
    print("3 Search")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        display_transactions()

    elif choice == "3":
        search_transactions()

    elif choice == "4":
        break