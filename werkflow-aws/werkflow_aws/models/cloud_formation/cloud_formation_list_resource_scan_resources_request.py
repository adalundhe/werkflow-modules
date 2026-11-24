from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListResourceScanResourcesRequest(BaseModel):
    ResourceScanId: StrictStr
    ResourceIdentifier: StrictStr | None = None
    ResourceTypePrefix: StrictStr | None = None
    TagKey: StrictStr | None = None
    TagValue: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
