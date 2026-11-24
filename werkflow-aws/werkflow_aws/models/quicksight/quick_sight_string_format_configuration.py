from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_null_value_format_configuration import QuickSightNullValueFormatConfiguration
from .quick_sight_numeric_format_configuration import QuickSightNumericFormatConfiguration


class QuickSightStringFormatConfiguration(BaseModel):
    NullValueFormatConfiguration: QuickSightNullValueFormatConfiguration | None = None
    NumericFormatConfiguration: QuickSightNumericFormatConfiguration | None = None
