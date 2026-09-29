import csv
from collections import defaultdict

class ReportService:
    def __init__(self, expense_service, budget_service):
        self.expenses = expense_service
        self.budgets = budget_service

    def total(self):
        return round(sum(e.amount for e in self.expenses.list_expenses()), 2)

    def category_totals(self):
        totals = defaultdict(float)
        for e in self.expenses.list_expenses():
            totals[e.category] += e.amount
        return dict(sorted(((k, round(v, 2)) for k, v in totals.items()), key=lambda x: x[1], reverse=True))

    def budget_status(self):
        spent = self.category_totals()
        rows = []
        for b in self.budgets.list_budgets():
            used = spent.get(b.category, 0.0)
            rows.append({"category": b.category, "budget": b.limit, "spent": used,
                         "remaining": round(b.limit - used, 2), "status": "OVER BUDGET" if used > b.limit else "OK"})
        return rows

    def export_csv(self, path):
        expenses = self.expenses.list_expenses()
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "amount", "category", "date", "note"])
            writer.writeheader()
            for e in expenses:
                writer.writerow(e.to_dict())
        return path
