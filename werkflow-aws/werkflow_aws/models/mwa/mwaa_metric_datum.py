from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .mwaa_dimension import MWAADimension
from .mwaa_statistic_set import MWAAStatisticSet


class MWAAMetricDatum(BaseModel):
    MetricName: StrictStr
    Timestamp: datetime.datetime | StrictStr
    Dimensions: list[MWAADimension] | None = None
    Value: StrictFloat | StrictInt | None = None
    Unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None'] | None = None
    StatisticValues: MWAAStatisticSet | None = None
