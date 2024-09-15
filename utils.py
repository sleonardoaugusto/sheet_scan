import os
from datetime import datetime


def file_exists(filename: str):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Error: The file '{filename}' does not exist.")


def convert_currency(value):
    value = (
        value.replace("\xa0", "").replace("R$", "").replace(".", "").replace(",", ".")
    )
    return float(value)


def convert_date(date_str):
    # Try to parse the date with different formats
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue

    raise ValueError("Date format not recognized. Please use '%d/%m/%Y' or '%Y-%m-%d'.")


def sort_rows_by_date(rows):
    # Sort rows by the date field, assuming the date is in the format "%d/%m/%Y" or similar
    return sorted(rows, key=lambda x: x.date)
