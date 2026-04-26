import json
import csv

data = [
    {"id": 1, "name": "Laptop", "value": 50000},
    {"id": 2, "name": "Phone", "value": 20000}
]

# Save JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Load JSON
try:
    with open("data.json", "r") as f:
        loaded = json.load(f)
        print("Loaded Data:", loaded)
except:
    print("Error loading file")

# Export CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Value"])

    for item in data:
        writer.writerow([item["id"], item["name"], item["value"]])

print("CSV file created")