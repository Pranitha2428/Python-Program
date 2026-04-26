transactions = []

while True:
    print("\nSmart Finance Manager")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        merchant = input("Enter merchant: ")

        transactions.append([date, amount, merchant])
        print("Transaction added!")

    elif choice == "2":
        print("\nTransactions List")
        for t in transactions:
            print(t)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")