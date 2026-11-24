from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetInsightRequest(BaseModel):
    InsightId: StrictStr
