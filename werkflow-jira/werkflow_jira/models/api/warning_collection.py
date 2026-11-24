from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WarningCollection(BaseModel):
    warnings: list[StrictStr] | None = None
