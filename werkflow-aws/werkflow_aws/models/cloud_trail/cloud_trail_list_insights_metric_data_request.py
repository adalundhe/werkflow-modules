from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailListInsightsMetricDataRequest(BaseModel):
    EventSource: StrictStr
    EventName: StrictStr
    InsightType: Literal['ApiCallRateInsight', 'ApiErrorRateInsight']
    TrailName: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Period: StrictInt | None = None
    DataType: Literal['FillWithZeros', 'NonZeroData'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
