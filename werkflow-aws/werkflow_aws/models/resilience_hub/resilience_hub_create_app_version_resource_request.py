from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_logical_resource_id import ResilienceHubLogicalResourceId


class ResilienceHubCreateAppVersionResourceRequest(BaseModel):
    appArn: StrictStr
    appComponents: list[StrictStr]
    logicalResourceId: ResilienceHubLogicalResourceId
    physicalResourceId: StrictStr
    resourceType: StrictStr
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    awsAccountId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    clientToken: StrictStr | None = None
    resourceName: StrictStr | None = None
