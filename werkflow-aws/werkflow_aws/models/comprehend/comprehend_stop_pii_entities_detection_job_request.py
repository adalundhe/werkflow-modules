from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopPiiEntitiesDetectionJobRequest(BaseModel):
    JobId: StrictStr
