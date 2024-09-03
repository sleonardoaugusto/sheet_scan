import pytest

from utils import convert_currency, file_exists


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
