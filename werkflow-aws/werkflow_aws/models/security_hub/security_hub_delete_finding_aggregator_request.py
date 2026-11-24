from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteFindingAggregatorRequest(BaseModel):
    FindingAggregatorArn: StrictStr
