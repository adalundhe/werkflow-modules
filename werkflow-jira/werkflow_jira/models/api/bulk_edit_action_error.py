from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BulkEditActionError(BaseModel):
    errorMessages: list[StrictStr] | None = None
    errors: dict[StrictStr, StrictStr] | None = None
