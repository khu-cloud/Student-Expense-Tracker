# Student Expense Tracker

A modular Python command-line application for recording, managing and analysing student expenses.

## Modules
1. **Expense Management** — add, view, update, delete and search expenses.
2. **Budget Management** — set category budgets and compare spending with limits.
3. **Reports & Export** — calculate total/category spending, show budget status and export CSV.

## Technologies
- Python 3.8+
- JSON file storage
- CSV export
- Python `unittest`
- Git/GitHub
- No external libraries

## Project Structure
```text
Student-Expense-Tracker/
├── main.py
├── config.py
├── models.py
├── storage.py
├── validators.py
├── expense_service.py
├── budget_service.py
├── report_service.py
├── ui.py
├── requirements.txt
├── statement.md
├── README.md
├── data/
│   ├── expenses.json
│   └── budgets.json
├── tests/
│   └── test_services.py
└── docs/
    └── design.md
```

## Installation & Run
1. Install Python 3.8 or later.
2. Clone/download the repository.
3. Open a terminal in the project folder.
4. Run:
```bash
python main.py
```

## Testing
Run:
```bash
python -m unittest discover -s tests -v
```

## Data
Expenses and budgets are stored locally in JSON files under `data/`. CSV export creates `expenses_export.csv` in the project root.

## Validation and Error Handling
The project validates names, amounts, categories and dates. Invalid input is caught by the console layer and reported without terminating the application.

## Academic Alignment
The project demonstrates modular programming, data structures, functions/classes, file handling, JSON storage, CRUD operations, validation, exception handling, testing and version-control-ready project organization.
