from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeKeyPhrasesDetectionJobRequest(BaseModel):
    JobId: StrictStr
