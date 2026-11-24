from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .textract_block import TextractBlock
from .textract_expense_field import TextractExpenseField
from .textract_line_item_group import TextractLineItemGroup


class TextractExpenseDocument(BaseModel):
    ExpenseIndex: StrictInt | None = None
    SummaryFields: list[TextractExpenseField] | None = None
    LineItemGroups: list[TextractLineItemGroup] | None = None
    Blocks: list[TextractBlock] | None = None
