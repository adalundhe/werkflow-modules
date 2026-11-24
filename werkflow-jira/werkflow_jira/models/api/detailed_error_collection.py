from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DetailedErrorCollection(BaseModel):
    details: dict[StrictStr, Any] | None = None
    errorMessages: list[StrictStr] | None = None
    errors: dict[StrictStr, StrictStr] | None = None
