from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .quick_sight_dynamic_default_value import QuickSightDynamicDefaultValue


class QuickSightIntegerDefaultValues(BaseModel):
    DynamicValue: QuickSightDynamicDefaultValue | None = None
    StaticValues: list[StrictInt] | None = None
