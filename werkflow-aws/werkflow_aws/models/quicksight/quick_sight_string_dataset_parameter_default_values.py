from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStringDatasetParameterDefaultValues(BaseModel):
    StaticValues: list[StrictStr] | None = None
