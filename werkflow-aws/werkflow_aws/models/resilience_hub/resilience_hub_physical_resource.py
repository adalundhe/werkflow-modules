from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .resilience_hub_app_component import ResilienceHubAppComponent
from .resilience_hub_logical_resource_id import ResilienceHubLogicalResourceId
from .resilience_hub_physical_resource_id import ResilienceHubPhysicalResourceId


class ResilienceHubPhysicalResource(BaseModel):
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    appComponents: list[ResilienceHubAppComponent] | None = None
    excluded: StrictBool | None = None
    logicalResourceId: ResilienceHubLogicalResourceId | None = None
    parentResourceName: StrictStr | None = None
    physicalResourceId: ResilienceHubPhysicalResourceId | None = None
    resourceName: StrictStr | None = None
    resourceType: StrictStr | None = None
    sourceType: StrictStr | None = None
