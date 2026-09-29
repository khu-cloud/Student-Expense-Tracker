from config import DATA_FILE, BUDGET_FILE
from storage import JsonStorage
from expense_service import ExpenseService
from budget_service import BudgetService
from report_service import ReportService
from ui import ConsoleUI

def build_app():
    expense_service = ExpenseService(JsonStorage(DATA_FILE))
    budget_service = BudgetService(JsonStorage(BUDGET_FILE))
    report_service = ReportService(expense_service, budget_service)
    return ConsoleUI(expense_service, budget_service, report_service)

if __name__ == "__main__":
    build_app().run()
