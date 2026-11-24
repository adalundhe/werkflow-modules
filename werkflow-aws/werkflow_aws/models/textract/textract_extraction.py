from __future__ import annotations
from pydantic import BaseModel
from .textract_expense_document import TextractExpenseDocument
from .textract_identity_document import TextractIdentityDocument
from .textract_lending_document import TextractLendingDocument


class TextractExtraction(BaseModel):
    LendingDocument: TextractLendingDocument | None = None
    ExpenseDocument: TextractExpenseDocument | None = None
    IdentityDocument: TextractIdentityDocument | None = None
