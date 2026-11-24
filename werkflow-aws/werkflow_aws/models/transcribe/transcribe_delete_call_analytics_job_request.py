from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteCallAnalyticsJobRequest(BaseModel):
    CallAnalyticsJobName: StrictStr
