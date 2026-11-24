from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_logical_resource_id import ResilienceHubLogicalResourceId


class ResilienceHubDescribeAppVersionResourceRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
    awsAccountId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    logicalResourceId: ResilienceHubLogicalResourceId | None = None
    physicalResourceId: StrictStr | None = None
    resourceName: StrictStr | None = None
