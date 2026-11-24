from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ValidationOptionsForUpdate(BaseModel):
    levels: list[StrictStr] | None = None
