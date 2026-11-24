from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_physical_resource_id import ResilienceHubPhysicalResourceId


class ResilienceHubResourceMapping(BaseModel):
    appRegistryAppName: StrictStr | None = None
    eksSourceName: StrictStr | None = None
    logicalStackName: StrictStr | None = None
    mappingType: StrictStr | None = None
    physicalResourceId: ResilienceHubPhysicalResourceId | None = None
    resourceGroupName: StrictStr | None = None
    resourceName: StrictStr | None = None
    terraformSourceName: StrictStr | None = None
