from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_resource_scan_summary import CloudFormationResourceScanSummary


class CloudFormationListResourceScansResponse(BaseModel):
    ResourceScanSummaries: list[CloudFormationResourceScanSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
