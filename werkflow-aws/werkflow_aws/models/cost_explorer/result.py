from pydantic import BaseModel, StrictStr, StrictBool
from .dimension_value_attribute import DimensionValueAttribute
from .result_group import ResultGroup
from .time_period import TimePeriod
from .total import Total

class Result(BaseModel):
    DimensionValueAttributes: list[DimensionValueAttribute]
    TimePeriod: TimePeriod
    Total: dict[StrictStr, Total]
    Groups: list[ResultGroup]
    Estimated: StrictBool
