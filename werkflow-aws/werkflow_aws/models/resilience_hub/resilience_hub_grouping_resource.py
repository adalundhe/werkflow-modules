from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_logical_resource_id import ResilienceHubLogicalResourceId
from .resilience_hub_physical_resource_id import ResilienceHubPhysicalResourceId


class ResilienceHubGroupingResource(BaseModel):
    logicalResourceId: ResilienceHubLogicalResourceId | None = None
    physicalResourceId: ResilienceHubPhysicalResourceId | None = None
    resourceName: StrictStr | None = None
    resourceType: StrictStr | None = None
    sourceAppComponentIds: list[StrictStr] | None = None
