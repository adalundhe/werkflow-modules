from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopEntitiesDetectionJobRequest(BaseModel):
    JobId: StrictStr
