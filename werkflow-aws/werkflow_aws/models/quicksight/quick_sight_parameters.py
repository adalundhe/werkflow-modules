from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_date_time_parameter import QuickSightDateTimeParameter
from .quick_sight_decimal_parameter import QuickSightDecimalParameter
from .quick_sight_integer_parameter import QuickSightIntegerParameter
from .quick_sight_string_parameter import QuickSightStringParameter


class QuickSightParameters(BaseModel):
    StringParameters: list[QuickSightStringParameter] | None = None
    IntegerParameters: list[QuickSightIntegerParameter] | None = None
    DecimalParameters: list[QuickSightDecimalParameter] | None = None
    DateTimeParameters: list[QuickSightDateTimeParameter] | None = None
