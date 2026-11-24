from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_aggregation_type import IoTAggregationType
from .io_t_tag import IoTTag


class IoTCreateFleetMetricRequest(BaseModel):
    metricName: StrictStr
    queryString: StrictStr
    aggregationType: IoTAggregationType
    period: StrictInt
    aggregationField: StrictStr
    description: StrictStr | None = None
    queryVersion: StrictStr | None = None
    indexName: StrictStr | None = None
    unit: Literal['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None'] | None = None
    tags: list[IoTTag] | None = None
