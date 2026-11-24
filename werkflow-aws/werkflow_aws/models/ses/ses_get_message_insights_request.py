from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetMessageInsightsRequest(BaseModel):
    MessageId: StrictStr
