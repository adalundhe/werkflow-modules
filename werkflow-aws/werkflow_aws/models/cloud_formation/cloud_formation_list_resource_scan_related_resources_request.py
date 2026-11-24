from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_formation_scanned_resource_identifier import CloudFormationScannedResourceIdentifier


class CloudFormationListResourceScanRelatedResourcesRequest(BaseModel):
    ResourceScanId: StrictStr
    Resources: list[CloudFormationScannedResourceIdentifier]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
