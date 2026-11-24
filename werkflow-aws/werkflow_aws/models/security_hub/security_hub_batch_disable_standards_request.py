from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubBatchDisableStandardsRequest(BaseModel):
    StandardsSubscriptionArns: list[StrictStr]
