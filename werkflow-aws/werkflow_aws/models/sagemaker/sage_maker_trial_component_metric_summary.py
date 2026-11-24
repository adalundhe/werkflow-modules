from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerTrialComponentMetricSummary(BaseModel):
    MetricName: StrictStr | None = None
    SourceArn: StrictStr | None = None
    TimeStamp: datetime.datetime | StrictStr | None = None
    Max: StrictFloat | StrictInt | None = None
    Min: StrictFloat | StrictInt | None = None
    Last: StrictFloat | StrictInt | None = None
    Count: StrictInt | None = None
    Avg: StrictFloat | StrictInt | None = None
    StdDev: StrictFloat | StrictInt | None = None
