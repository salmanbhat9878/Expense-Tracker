from datetime import datetime
from datetime import date
import json
import os
transactions = []

if os.path.exists("transactions.json"):
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
income = 0.0
expense = 0.0
for transaction in transactions:
    if transaction["type"] == "Income":
        income += transaction["amount"]
    elif transaction["type"] == "Expense":
        expense += transaction["amount"]
print("================================")
print("       EXPENSE TRACKER")
print("================================")

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Filter by Category")
    print("5. Filter by Date")
    print("6. Export to CSV")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Thank you for using Expense Tracker!")
        break
    elif choice == "1":
        try:
            amount = float(input("Enter income amount: "))
            if amount > 0:
                income += amount
                print("Income added successfully!")
                from datetime import date

                transactions.append({
                    "type": "Income",
                    "amount": amount,
                    "date": str(date.today())
                })

                with open("transactions.json", "w") as file:
                    json.dump(transactions, file, indent=4)
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        try:
            amount = float(input("Enter expense amount: "))

            if amount > 0:
                category = input(
                    "Enter category (Food, Travel, Shopping, Bills, Other): "
                ).strip()

                while category.lower() not in [
                    "food", "travel", "shopping", "bills", "other"
                ]:
                    print("Invalid category! Try again.")
                    category = input("Enter category: ").strip()

                expense += amount

                transactions.append({
                    "type": "Expense",
                    "amount": amount,
                    "category": category.title(),
                    "date": str(date.today())
                })

                with open("transactions.json", "w") as file:
                    json.dump(transactions, file, indent=4)

                print("Expense added successfully!")

            else:
                print("Amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        balance = income - expense
        print("\n--- Your Balance ---")
        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Remaining Balance:", balance)
    elif choice == "4":
        print("\n--- Filter by Category ---")

        category = input(
            "Enter category (Food, Travel, Shopping, Bills, Other): "
        ).strip()

        found = False

        for transaction in transactions:
            if (
                transaction["type"] == "Expense"
                and transaction.get("category", "").lower()
                == category.lower()
            ):
                print(transaction)
                found = True

        if not found:
            print("No transactions found in this category.")
    elif choice == "5":
        print("\n--- Filter by Date ---")

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
    elif choice == "6":
        print("\n--- Export Transactions to CSV ---")

        import csv

        with open("transactions.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["type", "amount", "category", "date"],
                extrasaction="ignore"
            )

            writer.writeheader()

            for transaction in transactions:
                writer.writerow(transaction)

        print("CSV file exported successfully!")
    else:
        print("Invalid choice! Please select 1-7.")