from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails(BaseModel):
    AvailabilityZoneCount: StrictInt | None = None
