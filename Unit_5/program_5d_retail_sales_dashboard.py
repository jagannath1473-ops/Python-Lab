import csv
from pathlib import Path

import matplotlib.pyplot as plt


sales_file = Path(__file__).with_name("sales.csv")
products = []
sales = []

with sales_file.open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row["Product"])
        sales.append(int(row["Sales"]))

plt.bar(products, sales)
plt.title("Retail Sales Dashboard")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(axis="y", alpha=0.3)
plt.show()
print("Retail sales dashboard displayed successfully")
Populate Python lab program contents
