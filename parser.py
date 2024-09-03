import enum
import re
from dataclasses import dataclass
from datetime import datetime

from utils import convert_date, convert_currency


@dataclass
class Row:
    date: datetime.date
    description: str
    installment: str
    amount: float


class Templates(str, enum.Enum):
    INTER = "inter"
    SANTANDER = "santander"


class InterBankParser:
    DATE_COL = 0
    DESCRIPTION_COL = 1
    INSTALLMENT_COL = 3
    AMOUNT_COL = 4

    def parse(self, row):
        return Row(
            date=self._parse_date(row),
            description=self._parse_description(row),
            installment=self._parse_installment(row),
            amount=self._parse_amount(row),
        )

    def _parse_date(self, row):
        text = row[self.DATE_COL]
        return convert_date(text)

    def _parse_description(self, row):
        return row[self.DESCRIPTION_COL]

    def _parse_installment(self, row):
        return row[self.INSTALLMENT_COL]

    def _parse_amount(self, row):
        text = row[self.AMOUNT_COL]
        return convert_currency(text)


class SantanderBankParser:
    DATE_COL = 0
    DESCRIPTION_COL = 1
    INSTALLMENT_COL = 1
    AMOUNT_COL = 3

    def parse(self, row):
        return Row(
            date=self._parse_date(row),
            description=self._parse_description(row),
            installment=self._parse_installment(row),
            amount=self._parse_amount(row),
        )

    def _parse_date(self, row):
        text = row[self.DATE_COL]
        return convert_date(text)

    def _parse_description(self, row):
        text = row[self.DESCRIPTION_COL]
        match = re.match(r"^(.*?)(?=\s*\(\d{1,2}/\d{1,2}\))", text)
        return match.group(1).strip() if match else text

    def _parse_installment(self, row):
        text = row[self.INSTALLMENT_COL]
        match = re.search(r"\((\d{1,2}/\d{1,2})\)", text)
        return match.group(1) if match else ""

    def _parse_amount(self, row):
        text = row[self.AMOUNT_COL]
        return convert_currency(text)


class ParserFactory:
    _mapping = {
        Templates.INTER: InterBankParser,
        Templates.SANTANDER: SantanderBankParser,
    }

    @classmethod
    def get_parser(cls, template):
        if template not in cls._mapping:
            raise ValueError(f"Unsupported template name: {template}")

        return cls._mapping[template]
