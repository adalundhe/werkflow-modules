from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetMonitoringSubscriptionRequest(BaseModel):
    DistributionId: StrictStr
