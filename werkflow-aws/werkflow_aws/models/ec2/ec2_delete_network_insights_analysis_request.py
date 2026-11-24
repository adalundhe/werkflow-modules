from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkInsightsAnalysisRequest(BaseModel):
    NetworkInsightsAnalysisId: StrictStr
    DryRun: StrictBool | None = None
