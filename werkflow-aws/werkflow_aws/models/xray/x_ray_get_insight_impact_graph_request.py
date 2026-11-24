from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class XRayGetInsightImpactGraphRequest(BaseModel):
    InsightId: StrictStr
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    NextToken: StrictStr | None = None
