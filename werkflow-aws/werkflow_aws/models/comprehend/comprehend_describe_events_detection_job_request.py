from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeEventsDetectionJobRequest(BaseModel):
    JobId: StrictStr
