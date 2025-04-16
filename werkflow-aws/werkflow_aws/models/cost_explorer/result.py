from pydantic import BaseModel, StrictStr, StrictBool
from .result_group import ResultGroup
from .time_period import TimePeriod
from .total import Total

class Result(BaseModel):
    TimePeriod: TimePeriod
    Total: dict[StrictStr, Total]
    Groups: list[ResultGroup]
    Estimated: StrictBool
