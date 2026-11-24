from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchGetInsightRuleReportRequest(BaseModel):
    RuleName: StrictStr
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    Period: StrictInt
    MaxContributorCount: StrictInt | None = None
    Metrics: list[StrictStr] | None = None
    OrderBy: StrictStr | None = None
