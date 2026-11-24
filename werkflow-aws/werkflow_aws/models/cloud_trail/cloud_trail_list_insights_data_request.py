from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailListInsightsDataRequest(BaseModel):
    InsightSource: StrictStr
    DataType: Literal['InsightsEvents']
    Dimensions: dict[Literal['EventId', 'EventName', 'EventSource'], StrictStr] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
