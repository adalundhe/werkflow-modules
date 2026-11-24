from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DevOpsGuruTimestampMetricValuePair(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    MetricValue: StrictFloat | StrictInt | None = None
