# -------- Transaction Module --------
def add_transaction(transactions):
    amount = float(input("Enter amount: "))
    merchant = input("Enter merchant: ")

    transactions.append({"amount": amount, "merchant": merchant})
    print("Transaction added")


# -------- Display Module --------
def display_transactions(transactions):
    print("\nTransactions:")
    for t in transactions:
        print(f"Amount: {t['amount']}, Merchant: {t['merchant']}")


# -------- Analysis Module --------
def total_spending(transactions):
    total = 0
    for t in transactions:
        total += t["amount"]
    print("Total Spending:", total)


# -------- Main Module --------
def main():
    transactions = []

    while True:
        print("\n1. Add")
        print("2. View")
        print("3. Total")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_transaction(transactions)

        elif ch == "2":
            display_transactions(transactions)

        elif ch == "3":
            total_spending(transactions)

        elif ch == "4":
            break

        else:
            print("Invalid choice")


main()