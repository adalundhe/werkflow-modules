from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailGetDistributionMetricDataRequest(BaseModel):
    distributionName: StrictStr
    metricName: Literal['Requests', 'BytesDownloaded', 'BytesUploaded', 'TotalErrorRate', 'Http4xxErrorRate', 'Http5xxErrorRate', 'WafAllowedRequests', 'WafBlockedRequests']
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    period: StrictInt
    unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None']
    statistics: list[Literal['Minimum', 'Maximum', 'Sum', 'Average', 'SampleCount']]
