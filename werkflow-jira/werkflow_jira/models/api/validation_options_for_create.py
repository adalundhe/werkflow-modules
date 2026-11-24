from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ValidationOptionsForCreate(BaseModel):
    levels: list[StrictStr] | None = None
