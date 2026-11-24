from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteAggregatorV2Request(BaseModel):
    AggregatorV2Arn: StrictStr
