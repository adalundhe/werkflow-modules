from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictStr


class SageMakerMetricData(BaseModel):
    MetricName: StrictStr | None = None
    Value: StrictFloat | None = None
    Timestamp: datetime.datetime | None = None
