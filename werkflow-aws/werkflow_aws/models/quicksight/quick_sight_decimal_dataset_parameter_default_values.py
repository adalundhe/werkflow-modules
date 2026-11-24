from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightDecimalDatasetParameterDefaultValues(BaseModel):
    StaticValues: list[StrictFloat | StrictInt] | None = None
