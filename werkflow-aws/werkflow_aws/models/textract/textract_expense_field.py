from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .textract_expense_currency import TextractExpenseCurrency
from .textract_expense_detection import TextractExpenseDetection
from .textract_expense_group_property import TextractExpenseGroupProperty
from .textract_expense_type import TextractExpenseType


class TextractExpenseField(BaseModel):
    Type: TextractExpenseType | None = None
    LabelDetection: TextractExpenseDetection | None = None
    ValueDetection: TextractExpenseDetection | None = None
    PageNumber: StrictInt | None = None
    Currency: TextractExpenseCurrency | None = None
    GroupProperties: list[TextractExpenseGroupProperty] | None = None
