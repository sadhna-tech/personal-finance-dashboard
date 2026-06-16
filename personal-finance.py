import pandas as pd
import matplotlib.pyplot as plt

transactions = []

while True:
    print("\n===== Personal Finance Dashboard =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Generate Expense Chart")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Income Amount: "))
        transactions.append({
            "Type": "Income",
            "Category": "Income",
            "Amount": amount
        })

    elif choice == "2":
        category = input(
            "Category (Food, Travel, Shopping, Bills): "
        )

        amount = float(input("Expense Amount: "))

        transactions.append({
            "Type": "Expense",
            "Category": category,
            "Amount": amount
        })

    elif choice == "3":
        if not transactions:
            print("No transactions found.")
            continue

        df = pd.DataFrame(transactions)

        income = df[df["Type"] == "Income"]["Amount"].sum()

        expense = df[df["Type"] == "Expense"]["Amount"].sum()

        balance = income - expense

        print("\n===== Financial Summary =====")
        print(f"Total Income: ₹{income}")
        print(f"Total Expense: ₹{expense}")
        print(f"Current Balance: ₹{balance}")

    elif choice == "4":
        if not transactions:
            print("No data available.")
            continue

        df = pd.DataFrame(transactions)

        expense_df = df[df["Type"] == "Expense"]

        if expense_df.empty:
            print("No expenses found.")
            continue

        expense_df.groupby(
            "Category"
        )["Amount"].sum().plot(
            kind="pie",
            autopct="%1.1f%%"
        )

        plt.title("Expense Distribution")
        plt.ylabel("")
        plt.show()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")