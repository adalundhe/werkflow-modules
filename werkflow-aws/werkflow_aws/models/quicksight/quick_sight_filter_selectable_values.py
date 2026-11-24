from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFilterSelectableValues(BaseModel):
    Values: list[StrictStr] | None = None
