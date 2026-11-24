from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudWatchInsightRuleContributorDatapoint(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    ApproximateValue: StrictFloat | StrictInt | None = None
