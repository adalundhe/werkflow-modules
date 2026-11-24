from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayVolumeRecoveryPointInfo(BaseModel):
    VolumeARN: StrictStr | None = None
    VolumeSizeInBytes: StrictInt | None = None
    VolumeUsageInBytes: StrictInt | None = None
    VolumeRecoveryPointTime: StrictStr | None = None
