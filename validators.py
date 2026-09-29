from datetime import datetime

class ValidationError(ValueError):
    pass

def validate_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValidationError("Expense name cannot be empty.")
    return name

def validate_amount(amount) -> float:
    try:
        value = float(amount)
    except (TypeError, ValueError):
        raise ValidationError("Amount must be a number.")
    if value <= 0:
        raise ValidationError("Amount must be greater than 0.")
    return round(value, 2)

def validate_category(category: str) -> str:
    category = category.strip().title()
    if not category:
        raise ValidationError("Category cannot be empty.")
    return category

def validate_date(date_text: str) -> str:
    try:
        date = datetime.strptime(date_text.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValidationError("Date must use YYYY-MM-DD format.")
    return date.strftime("%Y-%m-%d")
