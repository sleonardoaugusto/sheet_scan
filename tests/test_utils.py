from datetime import date

import pytest

from parser import Row
from utils import convert_currency, file_exists, sort_rows_by_date


def test_file_exists_when_file_exists(monkeypatch):
    """
    Should not raise a FileNotFoundError if the file exists
    """

    # Mock os.path.isfile to simulate that the file exists
    monkeypatch.setattr("os.path.isfile", lambda x: True)

    file_exists("existing_file.txt")


def test_file_exists_when_file_does_not_exists(monkeypatch):
    """
    Should raise a FileNotFoundError if the file does not exists
    """

    # Mock os.path.isfile to simulate that the file does not exists
    monkeypatch.setattr("os.path.isfile", lambda x: False)

    with pytest.raises(FileNotFoundError):
        file_exists("non_existing_file.txt")


def test_convert_currency():
    assert convert_currency("R$\xa01,23") == 1.23
    assert convert_currency("R$\xa012,34") == 12.34
    assert convert_currency("R$\xa0123,45") == 123.45
    assert convert_currency("R$\xa01.234,56") == 1234.56
    assert convert_currency("R$\xa012.345,67") == 12345.67


def test_sort_rows_by_date():
    row1 = Row(
        date=date(2024, 9, 12),
        description="Test1",
        amount=100,
        installment="",
    )
    row2 = Row(
        date=date(2024, 9, 11),
        description="Test2",
        amount=200,
        installment="",
    )
    row3 = Row(
        date=date(2024, 9, 13),
        description="Test3",
        amount=150,
        installment="",
    )

    unsorted_rows = [row1, row2, row3]
    expected_sorted_rows = [row2, row1, row3]

    assert sort_rows_by_date(unsorted_rows) == expected_sorted_rows
