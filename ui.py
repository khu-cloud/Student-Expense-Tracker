from validators import ValidationError

class ConsoleUI:
    def __init__(self, expense_service, budget_service, report_service):
        self.expenses = expense_service
        self.budgets = budget_service
        self.reports = report_service

    def run(self):
        while True:
            print("\n=== STUDENT EXPENSE TRACKER ===")
            print("1. Add expense\n2. View expenses\n3. Update expense\n4. Delete expense")
            print("5. Search expenses\n6. Set category budget\n7. Reports & budget status")
            print("8. Export CSV\n9. Exit")
            choice = input("Choose: ").strip()
            try:
                if choice == "1": self.add_expense()
                elif choice == "2": self.show(self.expenses.list_expenses())
                elif choice == "3": self.update_expense()
                elif choice == "4": self.delete_expense()
                elif choice == "5": self.search()
                elif choice == "6": self.set_budget()
                elif choice == "7": self.reports_menu()
                elif choice == "8": print(f"Exported to {self.reports.export_csv('expenses_export.csv')}")
                elif choice == "9": print("Goodbye!"); break
                else: print("Invalid choice.")
            except (ValidationError, ValueError) as e:
                print(f"Error: {e}")

    def add_expense(self):
        e = self.expenses.add(input("Name: "), input("Amount: "), input("Category: "), input("Date (YYYY-MM-DD, blank=today): "), input("Note: "))
        print(f"Added expense #{e.id}.")

    def update_expense(self):
        i = int(input("Expense ID: ")); old = next((e for e in self.expenses.list_expenses() if e.id == i), None)
        if not old: print("Expense not found."); return
        e = self.expenses.update(i, input(f"Name [{old.name}]: ") or old.name, input(f"Amount [{old.amount}]: ") or old.amount,
                                 input(f"Category [{old.category}]: ") or old.category, input(f"Date [{old.date}]: ") or old.date,
                                 input(f"Note [{old.note}]: ") or old.note)
        print(f"Updated expense #{e.id}.")

    def delete_expense(self):
        print("Deleted." if self.expenses.delete(int(input("Expense ID: "))) else "Expense not found.")

    def search(self):
        self.show(self.expenses.search(input("Category (blank=any): "), input("Keyword (blank=any): ")))

    def set_budget(self):
        b = self.budgets.set_budget(input("Category: "), input("Budget limit: "))
        print(f"Budget set: {b.category} = ₹{b.limit:.2f}")

    def reports_menu(self):
        print(f"\nTotal spending: ₹{self.reports.total():.2f}")
        print("By category:")
        for cat, amount in self.reports.category_totals().items(): print(f"  {cat}: ₹{amount:.2f}")
        print("Budget status:")
        for row in self.reports.budget_status(): print(f"  {row['category']}: spent ₹{row['spent']:.2f} / ₹{row['budget']:.2f} -> {row['status']}")

    @staticmethod
    def show(expenses):
        if not expenses: print("No expenses found."); return
        for e in expenses: print(f"#{e.id} | {e.date} | {e.category} | ₹{e.amount:.2f} | {e.name} | {e.note}")
