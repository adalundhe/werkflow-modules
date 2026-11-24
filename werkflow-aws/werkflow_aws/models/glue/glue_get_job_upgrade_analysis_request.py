from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetJobUpgradeAnalysisRequest(BaseModel):
    analysisId: StrictStr
    jobName: StrictStr
