class InvalidAmountError(Exception):
    pass

def check_amount(amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0")

try:
    amt = float(input("Enter amount: "))
    check_amount(amt)
    print("Valid amount entered")

except InvalidAmountError as e:
    print("Custom Error:", e)

except ValueError:
    print("Invalid input! Enter a number")

finally:
    print("Program finished")