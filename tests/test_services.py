import tempfile
from pathlib import Path
import unittest
from storage import JsonStorage
from expense_service import ExpenseService
from budget_service import BudgetService
from report_service import ReportService

class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.exp = ExpenseService(JsonStorage(root / "expenses.json"))
        self.bud = BudgetService(JsonStorage(root / "budgets.json"))
        self.rep = ReportService(self.exp, self.bud)

    def tearDown(self): self.tmp.cleanup()
      
    def test_add_and_total(self):
        self.exp.add("Lunch", 100, "Food", "2026-09-29")
        self.exp.add("Bus", 50, "Travel", "2026-09-29")
        self.assertEqual(self.rep.total(), 150)

    def test_category_search(self):
        self.exp.add("Notebook", 80, "Education", "2026-09-29")
        self.assertEqual(len(self.exp.search(category="education")), 1)

    def test_delete(self):
        e = self.exp.add("Tea", 20, "Food", "2026-09-29")
        self.assertTrue(self.exp.delete(e.id))
        self.assertEqual(len(self.exp.list_expenses()), 0)

    def test_budget_status(self):
        self.exp.add("Food", 120, "Food", "2026-09-29")
        self.bud.set_budget("Food", 100)
        self.assertEqual(self.rep.budget_status()[0]["status"], "OVER BUDGET")

if __name__ == "__main__": unittest.main()
