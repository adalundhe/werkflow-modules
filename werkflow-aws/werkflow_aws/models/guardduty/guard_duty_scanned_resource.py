from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_scanned_resource_details import GuardDutyScannedResourceDetails


class GuardDutyScannedResource(BaseModel):
    ScannedResourceArn: StrictStr | None = None
    ScannedResourceType: StrictStr | None = None
    ScannedResourceStatus: StrictStr | None = None
    ScanStatusReason: StrictStr | None = None
    ResourceDetails: GuardDutyScannedResourceDetails | None = None
