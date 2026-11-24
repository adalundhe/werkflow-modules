from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .resilience_hub_logical_resource_id import ResilienceHubLogicalResourceId


class ResilienceHubUpdateAppVersionResourceRequest(BaseModel):
    appArn: StrictStr
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    appComponents: list[StrictStr] | None = None
    awsAccountId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    excluded: StrictBool | None = None
    logicalResourceId: ResilienceHubLogicalResourceId | None = None
    physicalResourceId: StrictStr | None = None
    resourceName: StrictStr | None = None
    resourceType: StrictStr | None = None
