from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_date_time_dataset_parameter import QuickSightDateTimeDatasetParameter
from .quick_sight_decimal_dataset_parameter import QuickSightDecimalDatasetParameter
from .quick_sight_integer_dataset_parameter import QuickSightIntegerDatasetParameter
from .quick_sight_string_dataset_parameter import QuickSightStringDatasetParameter


class QuickSightDatasetParameter(BaseModel):
    StringDatasetParameter: QuickSightStringDatasetParameter | None = None
    DecimalDatasetParameter: QuickSightDecimalDatasetParameter | None = None
    IntegerDatasetParameter: QuickSightIntegerDatasetParameter | None = None
    DateTimeDatasetParameter: QuickSightDateTimeDatasetParameter | None = None
