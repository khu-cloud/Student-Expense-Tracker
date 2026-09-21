import json
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    """Load saved expenses from the JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n--- Add Expense ---")

    title = input("Enter expense name: ").strip()
    if not title:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category: ").strip()
    if not category:
        category = "Other"

    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded.")
        return

    print("-" * 70)
    print(f"{'No.':<5}{'Name':<20}{'Category':<15}{'Amount':>12}  Date")
    print("-" * 70)

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<5}"
            f"{expense['title'][:18]:<20}"
            f"{expense['category'][:13]:<15}"
            f"₹{expense['amount']:>10.2f}  "
            f"{expense['date']}"
        )

    print("-" * 70)


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spending: ₹{total:.2f}")


def search_category(expenses):
    print("\n--- Search by Category ---")

    if not expenses:
        print("No expenses recorded.")
        return

    category = input("Enter category: ").strip().lower()

    results = [
        expense for expense in expenses
        if expense["category"].lower() == category
    ]

    if not results:
        print("No expenses found in this category.")
        return

    category_total = sum(expense["amount"] for expense in results)

    print(f"\nExpenses in '{category}':")
    for i, expense in enumerate(results, start=1):
        print(
            f"{i}. {expense['title']} - "
            f"₹{expense['amount']:.2f} - {expense['date']}"
        )

    print(f"Category total: ₹{category_total:.2f}")


def delete_expense(expenses):
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))
        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    removed = expenses.pop(number - 1)
    save_expenses(expenses)

    print(f"Deleted: {removed['title']}")


def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 35)
        print("       STUDENT EXPENSE TRACKER")
        print("=" * 35)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Search by Category")
        print("5. Delete Expense")
        print("6. Exit")
        print("=" * 35)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            search_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Thank you for using Student Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
