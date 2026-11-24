from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateStorediSCSIVolumeRequest(BaseModel):
    GatewayARN: StrictStr
    DiskId: StrictStr
    PreserveExistingData: StrictBool
    TargetName: StrictStr
    NetworkInterfaceId: StrictStr
    SnapshotId: StrictStr | None = None
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
