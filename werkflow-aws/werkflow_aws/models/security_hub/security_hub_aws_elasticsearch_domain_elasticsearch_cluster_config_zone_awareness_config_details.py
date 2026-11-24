from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails(BaseModel):
    AvailabilityZoneCount: StrictInt | None = None
