from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .quick_sight_custom_parameter_values import QuickSightCustomParameterValues


class QuickSightCustomValuesConfiguration(BaseModel):
    IncludeNullValue: StrictBool | None = None
    CustomValues: QuickSightCustomParameterValues | None = None
