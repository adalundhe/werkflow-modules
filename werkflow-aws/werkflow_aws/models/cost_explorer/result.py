from pydantic import BaseModel, StrictStr, StrictBool
from .dimension_value_attribute import DimensionValueAttribute
from .period import Period
from .result_group import ResultGroup
from .total import Total

class Result(BaseModel):
    DimensionValueAttributes: list[DimensionValueAttribute]
    TimePeriod: Period | None = None
    Total: dict[StrictStr, Total]
    Groups: list[ResultGroup]
    Estimated: StrictBool
