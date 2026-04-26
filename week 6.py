# transaction.py

class Transaction:

    def __init__(self, tid, date, amount, t_type, merchant, category, notes):
        self.id = tid
        self.date = date
        self.amount = amount
        self.type = t_type
        self.merchant = merchant
        self.category = category
        self.notes = notes
        self.tags = set()

    def update_amount(self, new_amount):
        if new_amount > 0:
            self.amount = new_amount
            print("Amount updated")
        else:
            print("Invalid amount")

    def add_tag(self, tag):
        self.tags.add(tag)

    def classify(self):
        m = self.merchant.lower()

        if "swiggy" in m or "zomato" in m:
            self.category = "Food"

        elif "uber" in m or "ola" in m:
            self.category = "Transport"

        elif "amazon" in m:
            self.category = "Shopping"

        else:
            self.category = "Others"

    def display(self):
        print("\nTransaction Details")
        print("ID:", self.id)
        print("Date:", self.date)
        print("Amount:", self.amount)
        print("Type:", self.type)
        print("Merchant:", self.merchant)
        print("Category:", self.category)
        print("Tags:", self.tags)
        print("Notes:", self.notes)