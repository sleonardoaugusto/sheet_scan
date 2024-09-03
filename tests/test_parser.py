from datetime import datetime

import pytest

from main import read_sheet
from parser import Row, Templates


def test_template_constants():
    """Should return str instead of enum"""
    assert Templates.SANTANDER == "santander"
    assert Templates.INTER == "inter"


class TestInterBankParser:
    @pytest.fixture
    def mock_sheet(self):
        return iter(
            [
                ["Data", "Lançamento", "Categoria", "Tipo", "Valor"],
                [
                    "14/05/2024",
                    "Jetbrains Americas I",
                    "OUTROS",
                    "Compra à vista",
                    "R$\xa0315,46",
                ],
                [
                    "14/05/2024",
                    "Iof Internacional",
                    "OUTROS",
                    "Parcela 1/10",
                    "R$\xa013,82",
                ],
            ]
        )

    def test_read_sheet(self, mock_sheet):
        """
        Assert that headers should be ignored and rows should be returned in the correct format.

        Args:
            mock_sheet (iterator): Fixture providing the mock sheet data.

        Asserts:
            The processed data matches the expected result.
        """
        expected = [
            Row(
                date=datetime(2024, 5, 14).date(),
                description="Jetbrains Americas I",
                installment="Compra à vista",
                amount=315.46,
            ),
            Row(
                date=datetime(2024, 5, 14).date(),
                description="Iof Internacional",
                installment="Parcela 1/10",
                amount=13.82,
            ),
        ]
        assert read_sheet(mock_sheet, Templates.INTER) == expected


class TestSantanderBankParser:
    @pytest.fixture
    def mock_sheet(self):
        return iter(
            [
                ["Lançamentos", "", "", ""],
                ["Cartão", "Final 0001", "", ""],
                ["Titular", "LEONARDO A SILVA", "", ""],
                ["Data", "Descrição", "Valor (US$)", "Valor (R$)"],
                [
                    "14/05/2024",
                    "Mercearia",
                    "0",
                    "26",
                ],
                ["Cartão", "Final 0002", "", ""],
                ["Titular", "LEONARDO AUGUSTO S", "", ""],
                ["Data", "Descrição", "Valor (US$)", "Valor (R$)"],
                [
                    "30/08/2024",
                    "Moveis & Decor (12/12)",
                    "0",
                    "226,45",
                ],
                ["", "", "", ""],
                ["", "Resumo de despesas", "", ""],
            ]
        )

    def test_read_sheet(self, mock_sheet):
        """
        Assert that headers should be ignored and rows should be returned in the correct format.

        Args:
            mock_sheet (iterator): Fixture providing the mock sheet data.

        Asserts:
            The processed data matches the expected result.
        """
        expected = [
            Row(
                date=datetime(2024, 5, 14).date(),
                description="Mercearia",
                installment="",
                amount=26.0,
            ),
            Row(
                date=datetime(2024, 8, 30).date(),
                description="Moveis & Decor",
                installment="12/12",
                amount=226.45,
            ),
        ]
        assert read_sheet(mock_sheet, Templates.SANTANDER) == expected
