from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeTargetedSentimentDetectionJobRequest(BaseModel):
    JobId: StrictStr
