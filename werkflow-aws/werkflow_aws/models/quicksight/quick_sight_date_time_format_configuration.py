from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_null_value_format_configuration import QuickSightNullValueFormatConfiguration
from .quick_sight_numeric_format_configuration import QuickSightNumericFormatConfiguration


class QuickSightDateTimeFormatConfiguration(BaseModel):
    DateTimeFormat: StrictStr | None = None
    NullValueFormatConfiguration: QuickSightNullValueFormatConfiguration | None = None
    NumericFormatConfiguration: QuickSightNumericFormatConfiguration | None = None
