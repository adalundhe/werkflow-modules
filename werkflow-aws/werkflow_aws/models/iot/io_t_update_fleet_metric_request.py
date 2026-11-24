from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_aggregation_type import IoTAggregationType


class IoTUpdateFleetMetricRequest(BaseModel):
    metricName: StrictStr
    indexName: StrictStr
    queryString: StrictStr | None = None
    aggregationType: IoTAggregationType | None = None
    period: StrictInt | None = None
    aggregationField: StrictStr | None = None
    description: StrictStr | None = None
    queryVersion: StrictStr | None = None
    unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None'] | None = None
    expectedVersion: StrictInt | None = None
