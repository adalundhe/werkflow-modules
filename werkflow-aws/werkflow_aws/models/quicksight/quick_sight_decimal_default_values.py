from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .quick_sight_dynamic_default_value import QuickSightDynamicDefaultValue


class QuickSightDecimalDefaultValues(BaseModel):
    DynamicValue: QuickSightDynamicDefaultValue | None = None
    StaticValues: list[StrictFloat | StrictInt] | None = None
