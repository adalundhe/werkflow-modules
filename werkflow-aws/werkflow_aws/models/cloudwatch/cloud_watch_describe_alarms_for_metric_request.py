from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_dimension_model import CloudWatchDimensionModel


class CloudWatchDescribeAlarmsForMetricRequest(BaseModel):
    MetricName: StrictStr
    Namespace: StrictStr
    Statistic: Literal['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum'] | None = None
    ExtendedStatistic: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
    Period: StrictInt | None = None
    Unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None'] | None = None
