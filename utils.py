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


def convert_date(value):
    try:
        return datetime.strptime(value, "%d/%m/%Y").date()

    except ValueError:
        raise ValueError(f"Error: The date: {value} is not a valid date.")
