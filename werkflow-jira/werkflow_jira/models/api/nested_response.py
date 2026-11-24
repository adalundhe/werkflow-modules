from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .error_collection import ErrorCollection
from .warning_collection import WarningCollection


class NestedResponse(BaseModel):
    errorCollection: ErrorCollection | None = None
    status: StrictInt | None = None
    warningCollection: WarningCollection | None = None
