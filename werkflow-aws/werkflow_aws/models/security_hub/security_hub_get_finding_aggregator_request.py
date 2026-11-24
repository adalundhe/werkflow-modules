from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetFindingAggregatorRequest(BaseModel):
    FindingAggregatorArn: StrictStr
