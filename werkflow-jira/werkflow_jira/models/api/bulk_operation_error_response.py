from __future__ import annotations
from pydantic import BaseModel
from .error_message import ErrorMessage


class BulkOperationErrorResponse(BaseModel):
    errors: list[ErrorMessage] | None = None
