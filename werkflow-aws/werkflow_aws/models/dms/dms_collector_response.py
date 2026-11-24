from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_collector_health_check import DMSCollectorHealthCheck
from .dms_inventory_data import DMSInventoryData


class DMSCollectorResponse(BaseModel):
    CollectorReferencedId: StrictStr | None = None
    CollectorName: StrictStr | None = None
    CollectorVersion: StrictStr | None = None
    VersionStatus: StrictStr | None = None
    Description: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    CollectorHealthCheck: DMSCollectorHealthCheck | None = None
    LastDataReceived: StrictStr | None = None
    RegisteredDate: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    ModifiedDate: StrictStr | None = None
    InventoryData: DMSInventoryData | None = None
