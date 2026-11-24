from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListMetricValuesRequest(BaseModel):
    thingName: StrictStr
    metricName: StrictStr
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    dimensionName: StrictStr | None = None
    dimensionValueOperator: Literal['IN', 'NOT_IN'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
