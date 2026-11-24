from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteMonitoringSubscriptionRequest(BaseModel):
    DistributionId: StrictStr
