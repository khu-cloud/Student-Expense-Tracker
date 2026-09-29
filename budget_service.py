from models import Budget
from validators import validate_amount, validate_category

class BudgetService:
    def __init__(self, storage):
        self.storage = storage

    def _all(self):
        return {x["category"]: Budget(str(x["category"]), float(x["limit"])) for x in self.storage.read()}

    def set_budget(self, category, limit):
        category = validate_category(category)
        budgets = self._all()
        budgets[category] = Budget(category, validate_amount(limit))
        self.storage.write([b.to_dict() for b in budgets.values()])
        return budgets[category]

    def list_budgets(self):
        return list(self._all().values())

    def get_limit(self, category):
        budget = self._all().get(category.title())
        return budget.limit if budget else None
