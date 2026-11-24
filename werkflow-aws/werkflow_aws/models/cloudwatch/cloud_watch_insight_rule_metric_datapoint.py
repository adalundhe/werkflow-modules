from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudWatchInsightRuleMetricDatapoint(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    UniqueContributors: StrictFloat | StrictInt | None = None
    MaxContributorValue: StrictFloat | StrictInt | None = None
    SampleCount: StrictFloat | StrictInt | None = None
    Average: StrictFloat | StrictInt | None = None
    Sum: StrictFloat | StrictInt | None = None
    Minimum: StrictFloat | StrictInt | None = None
    Maximum: StrictFloat | StrictInt | None = None
