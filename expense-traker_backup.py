from datetime import datetime
import json
import os
import csv
print("================================")
print("       EXPENSE TRACKER")
print("================================")
print("1. Add Income")
print("2. Add Expense")
print("3. View Balance")
print("4. Exit")
income = 0.0

while True:
    try:
        amount = float(input("Enter income amount: "))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid amount! Please enter a number.")
income = income + amount

print("Income added:", income)
expense = 0.0

while True:
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid amount! Please enter a number.")
expense = expense + amount

print("Expense added:", expense)
balance = income - expense
print("Remaining Balance:", balance)
from datetime import date

today = date.today()
print("Transaction Date:", today)
print("\nExpense Categories:")
print("1. Food")
print("2. Travel")
print("3. Shopping")
print("4. Bills")
print("5. Other")
category = input("Choose expense category (1-5): ")

categories = {
    "1": "Food",
    "2": "Travel",
    "3": "Shopping",
    "4": "Bills",
    "5": "Other"
}

if category in categories:
    print("Selected Category:", categories[category])
else:
    print("Invalid category! Please choose 1-5.")
transactions = [
    {
        "type": "Income",
        "amount": income,
        "date": str(today)
    },
    {
        "type": "Expense",

        "amount": expense,
        "category": categories.get(category, "Other"),
        "date": str(today)
    }
]
if os.path.exists("transactions.json"):
    with open("transactions.json", "r") as file:
        old_transactions = json.load(file)
    transactions = old_transactions + transactions

with open("transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)

print("Transactions saved successfully!")

print("\n--- Filter Transactions by Category ---")

filter_category = input("Enter category (Food, Travel, Shopping, Bills, Other): ").strip()

found = False

for transaction in transactions:
    if (transaction["type"] == "Expense"
            and transaction.get("category", "").lower() == filter_category.lower()):
        print(transaction)
        found = True

if not found:
    print("No transactions found in this category.")


print("\n--- Filter Transactions by Date ---")

start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

try:
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    if start > end:
        print("Start date cannot be after end date.")
    else:
        found = False

        for transaction in transactions:
            transaction_date = datetime.strptime(
                transaction["date"], "%Y-%m-%d"
            ).date()

            if start <= transaction_date <= end:
                print(transaction)
                found = True

        if not found:
            print("No transactions found in this date range.")

except ValueError:
    print("Invalid date! Please use YYYY-MM-DD.")

print("\n--- Export Transactions to CSV ---")

with open("transactions.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["type", "amount", "category", "date"]
    )
    writer.writeheader()
    writer.writerows(transactions)

print("CSV file exported successfully!")