from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateCachediSCSIVolumeRequest(BaseModel):
    GatewayARN: StrictStr
    VolumeSizeInBytes: StrictInt
    TargetName: StrictStr
    NetworkInterfaceId: StrictStr
    ClientToken: StrictStr
    SnapshotId: StrictStr | None = None
    SourceVolumeARN: StrictStr | None = None
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
