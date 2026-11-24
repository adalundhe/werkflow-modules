from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightIntegerDatasetParameterDefaultValues(BaseModel):
    StaticValues: list[StrictInt] | None = None
