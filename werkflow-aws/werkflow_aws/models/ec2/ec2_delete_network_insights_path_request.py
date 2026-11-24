from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkInsightsPathRequest(BaseModel):
    NetworkInsightsPathId: StrictStr
    DryRun: StrictBool | None = None
