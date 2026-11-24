from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopEventsDetectionJobRequest(BaseModel):
    JobId: StrictStr
