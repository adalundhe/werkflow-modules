from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LightsailMetricDatapoint(BaseModel):
    average: StrictFloat | StrictInt | None = None
    maximum: StrictFloat | StrictInt | None = None
    minimum: StrictFloat | StrictInt | None = None
    sampleCount: StrictFloat | StrictInt | None = None
    sum: StrictFloat | StrictInt | None = None
    timestamp: datetime.datetime | StrictStr | None = None
    unit: StrictStr | None = None
