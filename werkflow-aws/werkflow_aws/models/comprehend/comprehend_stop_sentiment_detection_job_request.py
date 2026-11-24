from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopSentimentDetectionJobRequest(BaseModel):
    JobId: StrictStr
