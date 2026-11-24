from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetInsightSelectorsRequest(BaseModel):
    TrailName: StrictStr | None = None
    EventDataStore: StrictStr | None = None
