from __future__ import annotations
from pydantic import BaseModel
from .textract_expense_field import TextractExpenseField


class TextractLineItemFields(BaseModel):
    LineItemExpenseFields: list[TextractExpenseField] | None = None
