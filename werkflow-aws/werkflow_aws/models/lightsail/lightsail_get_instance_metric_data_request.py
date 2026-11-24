from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailGetInstanceMetricDataRequest(BaseModel):
    instanceName: StrictStr
    metricName: Literal['CPUUtilization', 'NetworkIn', 'NetworkOut', 'StatusCheckFailed', 'StatusCheckFailed_Instance', 'StatusCheckFailed_System', 'BurstCapacityTime', 'BurstCapacityPercentage', 'MetadataNoToken', 'DiskReadOps', 'DiskWriteOps', 'DiskReadBytes', 'DiskWriteBytes', 'DiskTotalReadTime', 'DiskTotalWriteTime', 'DiskQueueLength']
    period: StrictInt
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None']
    statistics: list[Literal['Minimum', 'Maximum', 'Sum', 'Average', 'SampleCount']]
