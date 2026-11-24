from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeEntitiesDetectionJobRequest(BaseModel):
    JobId: StrictStr
