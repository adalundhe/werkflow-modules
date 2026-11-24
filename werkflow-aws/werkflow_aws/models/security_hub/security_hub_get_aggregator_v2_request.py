from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetAggregatorV2Request(BaseModel):
    AggregatorV2Arn: StrictStr
