from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayAttachVolumeRequest(BaseModel):
    GatewayARN: StrictStr
    VolumeARN: StrictStr
    NetworkInterfaceId: StrictStr
    TargetName: StrictStr | None = None
    DiskId: StrictStr | None = None
