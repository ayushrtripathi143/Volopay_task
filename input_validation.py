from turtle import pd


def validate_date(date):
    try:
        pd.to_datetime(date)
    except ValueError:
        raise ValueError("Invalid date format. Date should be in the format 'YYYY-MM-DD'.")

def validate_department(department):
    valid_departments = ['marketing', 'sales', 'finance']  # Add more valid department names if needed
    if department not in valid_departments:
        raise ValueError("Invalid department. Valid department names are: " + ", ".join(valid_departments) + ".")

def validate_item_by(item_by):
    valid_item_by = ['quantity', 'price']
    if item_by not in valid_item_by:
        raise ValueError("Invalid item_by parameter. Valid options are: " + ", ".join(valid_item_by) + ".")

def validate_n(n):
    if n <= 0:
        raise ValueError("Invalid n parameter. n should be a positive integer.")
