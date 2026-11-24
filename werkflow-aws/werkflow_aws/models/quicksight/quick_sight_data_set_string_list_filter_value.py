from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSetStringListFilterValue(BaseModel):
    StaticValues: list[StrictStr] | None = None
