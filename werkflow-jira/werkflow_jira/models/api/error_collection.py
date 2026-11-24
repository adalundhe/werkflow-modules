from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ErrorCollection(BaseModel):
    errorMessages: list[StrictStr] | None = None
    errors: dict[StrictStr, StrictStr] | None = None
    status: StrictInt | None = None
