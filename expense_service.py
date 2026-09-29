from datetime import date
from models import Expense
from validators import validate_name, validate_amount, validate_category, validate_date

class ExpenseService:
    def __init__(self, storage):
        self.storage = storage

    def _all(self):
        return [Expense.from_dict(x) for x in self.storage.read()]

    def list_expenses(self):
        return sorted(self._all(), key=lambda e: (e.date, e.id), reverse=True)

    def add(self, name, amount, category, date_text=None, note=""):
        expenses = self._all()
        new_id = max((e.id for e in expenses), default=0) + 1
        expense = Expense(new_id, validate_name(name), validate_amount(amount),
                          validate_category(category),
                          validate_date(date_text or date.today().isoformat()), note.strip())
        expenses.append(expense)
        self.storage.write([e.to_dict() for e in expenses])
        return expense

    def delete(self, expense_id):
        expenses = self._all()
        remaining = [e for e in expenses if e.id != int(expense_id)]
        if len(remaining) == len(expenses):
            return False
        self.storage.write([e.to_dict() for e in remaining])
        return True

    def update(self, expense_id, name, amount, category, date_text, note=""):
        expenses = self._all()
        for i, e in enumerate(expenses):
            if e.id == int(expense_id):
                expenses[i] = Expense(e.id, validate_name(name), validate_amount(amount),
                                      validate_category(category), validate_date(date_text), note.strip())
                self.storage.write([x.to_dict() for x in expenses])
                return expenses[i]
        return None

    def search(self, category=None, keyword=None):
        result = self.list_expenses()
        if category:
            result = [e for e in result if e.category.lower() == category.strip().lower()]
        if keyword:
            k = keyword.strip().lower()
            result = [e for e in result if k in e.name.lower() or k in e.note.lower()]
        return result
