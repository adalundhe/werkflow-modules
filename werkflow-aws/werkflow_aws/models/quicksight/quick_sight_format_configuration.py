from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_date_time_format_configuration import QuickSightDateTimeFormatConfiguration
from .quick_sight_number_format_configuration import QuickSightNumberFormatConfiguration
from .quick_sight_string_format_configuration import QuickSightStringFormatConfiguration


class QuickSightFormatConfiguration(BaseModel):
    StringFormatConfiguration: QuickSightStringFormatConfiguration | None = None
    NumberFormatConfiguration: QuickSightNumberFormatConfiguration | None = None
    DateTimeFormatConfiguration: QuickSightDateTimeFormatConfiguration | None = None
