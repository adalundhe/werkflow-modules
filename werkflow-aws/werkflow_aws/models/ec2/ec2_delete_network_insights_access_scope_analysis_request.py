from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkInsightsAccessScopeAnalysisRequest(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: StrictStr
    DryRun: StrictBool | None = None
