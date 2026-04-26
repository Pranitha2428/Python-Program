from datetime import datetime
# Base Class
class Record:
    def __init__(self):
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

    def update_timestamp(self):
        self._updated_at = datetime.now()

    def show_time(self):
        print("Created:", self._created_at)
        print("Updated:", self._updated_at)


# Child Class 1: Complaint
class Complaint(Record):
    def __init__(self, cid, issue):
        super().__init__()
        self.id = cid
        self._issue = issue   # protected attribute

    def update_issue(self, new_issue):
        self._issue = new_issue
        self.update_timestamp()

    def display(self):
        print("\n--- Complaint Details ---")
        print("ID:", self.id)
        print("Issue:", self._issue)
        self.show_time()


# Child Class 2: Asset
class Asset(Record):
    def __init__(self, aid, name, value):
        super().__init__()
        self.id = aid
        self.name = name
        self.__value = value   # private attribute

    def update_value(self, new_value):
        self.__value = new_value
        self.update_timestamp()

    def get_value(self):
        return self.__value

    def display(self):
        print("\n--- Asset Details ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Value:", self.__value)
        self.show_time()


# ---------------- MAIN PROGRAM ----------------

# Create objects
c1 = Complaint(101, "Fan not working")
a1 = Asset(201, "Laptop", 50000)

# Display initial data
c1.display()
a1.display()

# Update data
c1.update_issue("Fan making noise")
a1.update_value(55000)

# Display updated data
print("\nAfter Updates:")
c1.display()
a1.display()