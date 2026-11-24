from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneColumnFilterConfiguration(BaseModel):
    includedColumnNames: list[StrictStr] | None = None
