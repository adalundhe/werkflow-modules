from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkInsightsAccessScopeRequest(BaseModel):
    NetworkInsightsAccessScopeId: StrictStr
    DryRun: StrictBool | None = None
