from datetime import datetime
from finance_tracker.config import (
    DEFAULT_CATEGORIES,
    MIN_AMOUNT,
    MAX_AMOUNT,
    MAX_DESCRIPTION_LENGTH,
    DATE_FORMAT
)

class ValidationError(Exception):
    pass

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount < MIN_AMOUNT:
            raise ValidationError(f"Amount must be at least ₹{MIN_AMOUNT}")
        if amount > MAX_AMOUNT:
            raise ValidationError(f"Amount cannot exceed ₹{MAX_AMOUNT}")
        return amount
    except ValueError:
        raise ValidationError("Invalid amount. Please enter a valid number.")

def validate_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return date_str
    except ValueError:
        raise ValidationError(f"Invalid date format. Use {DATE_FORMAT} (e.g., 2024-01-15)")

def validate_category(category):
    if category not in DEFAULT_CATEGORIES:
        raise ValidationError(f"Invalid category. Choose from: {', '.join(DEFAULT_CATEGORIES)}")
    return category

def validate_description(description):
    if not description or not description.strip():
        raise ValidationError("Description cannot be empty")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        raise ValidationError(f"Description too long. Maximum {MAX_DESCRIPTION_LENGTH} characters.")
    return description.strip()

def get_validated_input(prompt, validator):
    while True:
        try:
            user_input = input(prompt).strip()
            return validator(user_input)
        except ValidationError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None