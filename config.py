from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "expenses.json"
BUDGET_FILE = DATA_DIR / "budgets.json"
CURRENCY = "INR"
DEFAULT_CATEGORIES = ["Food", "Travel", "Education", "Shopping", "Entertainment", "Bills", "Other"]
