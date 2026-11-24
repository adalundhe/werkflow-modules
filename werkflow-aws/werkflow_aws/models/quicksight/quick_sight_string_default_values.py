from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dynamic_default_value import QuickSightDynamicDefaultValue


class QuickSightStringDefaultValues(BaseModel):
    DynamicValue: QuickSightDynamicDefaultValue | None = None
    StaticValues: list[StrictStr] | None = None
