from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_logical_resource_id import ResilienceHubLogicalResourceId


class ResilienceHubResourceIdentifier(BaseModel):
    logicalResourceId: ResilienceHubLogicalResourceId | None = None
    resourceType: StrictStr | None = None
