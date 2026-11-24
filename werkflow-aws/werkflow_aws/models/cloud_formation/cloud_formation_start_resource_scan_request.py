from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_scan_filter import CloudFormationScanFilter


class CloudFormationStartResourceScanRequest(BaseModel):
    ClientRequestToken: StrictStr | None = None
    ScanFilters: list[CloudFormationScanFilter] | None = None
