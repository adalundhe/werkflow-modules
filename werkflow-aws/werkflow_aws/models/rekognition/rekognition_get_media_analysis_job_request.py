from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionGetMediaAnalysisJobRequest(BaseModel):
    JobId: StrictStr
