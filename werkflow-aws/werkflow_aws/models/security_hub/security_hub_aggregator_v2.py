from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAggregatorV2(BaseModel):
    AggregatorV2Arn: StrictStr | None = None
