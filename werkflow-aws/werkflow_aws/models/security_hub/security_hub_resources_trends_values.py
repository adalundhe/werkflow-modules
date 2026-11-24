from __future__ import annotations
from pydantic import BaseModel
from .security_hub_resources_count import SecurityHubResourcesCount


class SecurityHubResourcesTrendsValues(BaseModel):
    ResourcesCount: SecurityHubResourcesCount | None = None
