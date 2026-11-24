from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeDominantLanguageDetectionJobRequest(BaseModel):
    JobId: StrictStr
