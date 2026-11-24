from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailGetContainerServiceMetricDataRequest(BaseModel):
    serviceName: StrictStr
    metricName: Literal['CPUUtilization', 'MemoryUtilization']
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    period: StrictInt
    statistics: list[Literal['Minimum', 'Maximum', 'Sum', 'Average', 'SampleCount']]
