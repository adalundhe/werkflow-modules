from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_decimal_places_configuration import QuickSightDecimalPlacesConfiguration
from .quick_sight_negative_value_configuration import QuickSightNegativeValueConfiguration
from .quick_sight_null_value_format_configuration import QuickSightNullValueFormatConfiguration
from .quick_sight_numeric_separator_configuration import QuickSightNumericSeparatorConfiguration


class QuickSightNumberDisplayFormatConfiguration(BaseModel):
    Prefix: StrictStr | None = None
    Suffix: StrictStr | None = None
    SeparatorConfiguration: QuickSightNumericSeparatorConfiguration | None = None
    DecimalPlacesConfiguration: QuickSightDecimalPlacesConfiguration | None = None
    NumberScale: StrictStr | None = None
    NegativeValueConfiguration: QuickSightNegativeValueConfiguration | None = None
    NullValueFormatConfiguration: QuickSightNullValueFormatConfiguration | None = None
