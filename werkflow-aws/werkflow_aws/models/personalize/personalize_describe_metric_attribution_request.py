from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeMetricAttributionRequest(BaseModel):
    metricAttributionArn: StrictStr
