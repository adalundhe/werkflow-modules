from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .error_collection import ErrorCollection


class BulkOperationErrorResult(BaseModel):
    elementErrors: ErrorCollection | None = None
    failedElementNumber: StrictInt | None = None
    status: StrictInt | None = None
