from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerMetricDataModel(BaseModel):
    MetricName: StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
