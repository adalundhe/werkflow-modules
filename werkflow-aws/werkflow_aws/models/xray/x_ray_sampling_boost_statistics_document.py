from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class XRaySamplingBoostStatisticsDocument(BaseModel):
    RuleName: StrictStr
    ServiceName: StrictStr
    Timestamp: datetime.datetime | StrictStr
    AnomalyCount: StrictInt
    TotalCount: StrictInt
    SampledAnomalyCount: StrictInt
