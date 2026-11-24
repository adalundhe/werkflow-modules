from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_scanned_resource import CloudFormationScannedResource


class CloudFormationListResourceScanResourcesResponse(BaseModel):
    Resources: list[CloudFormationScannedResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
