from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailGetLoadBalancerMetricDataRequest(BaseModel):
    loadBalancerName: StrictStr
    metricName: Literal['ClientTLSNegotiationErrorCount', 'HealthyHostCount', 'UnhealthyHostCount', 'HTTPCode_LB_4XX_Count', 'HTTPCode_LB_5XX_Count', 'HTTPCode_Instance_2XX_Count', 'HTTPCode_Instance_3XX_Count', 'HTTPCode_Instance_4XX_Count', 'HTTPCode_Instance_5XX_Count', 'InstanceResponseTime', 'RejectedConnectionCount', 'RequestCount']
    period: StrictInt
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None']
    statistics: list[Literal['Minimum', 'Maximum', 'Sum', 'Average', 'SampleCount']]
