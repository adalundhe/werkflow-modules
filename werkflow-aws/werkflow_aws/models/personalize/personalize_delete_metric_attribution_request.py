from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteMetricAttributionRequest(BaseModel):
    metricAttributionArn: StrictStr
