transactions = []

def add_transaction():
    tid = int(input("Enter transaction ID: "))
    date = input("Enter date: ")
    amount = float(input("Enter amount: "))
    t_type = input("Enter type (credit/debit): ")
    merchant = input("Enter merchant: ")
    category = input("Enter category: ")
    notes = input("Enter notes: ")

    tags = input("Enter tags separated by comma: ")
    tag_set = set(tags.split(","))

    transaction = {
        "id": tid,
        "date": date,
        "amount": amount,
        "type": t_type,
        "merchant": merchant,
        "category": category,
        "tags": tag_set,
        "notes": notes
    }

    transactions.append(transaction)
    print("Transaction added!")

def view_transactions():
    for t in transactions:
        print("\nTransaction ID:", t["id"])
        print("Date:", t["date"])
        print("Amount:", t["amount"])
        print("Type:", t["type"])
        print("Merchant:", t["merchant"])
        print("Category:", t["category"])
        print("Tags:", t["tags"])
        print("Notes:", t["notes"])

while True:
    print("\n1 Add Transaction")
    print("2 View Transactions")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        break