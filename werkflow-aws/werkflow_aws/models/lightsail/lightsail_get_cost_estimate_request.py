from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailGetCostEstimateRequest(BaseModel):
    resourceName: StrictStr
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
