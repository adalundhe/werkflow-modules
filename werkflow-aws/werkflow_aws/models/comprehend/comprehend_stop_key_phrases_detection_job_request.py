from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopKeyPhrasesDetectionJobRequest(BaseModel):
    JobId: StrictStr
