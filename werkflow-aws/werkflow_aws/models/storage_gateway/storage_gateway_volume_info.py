from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayVolumeInfo(BaseModel):
    VolumeARN: StrictStr | None = None
    VolumeId: StrictStr | None = None
    GatewayARN: StrictStr | None = None
    GatewayId: StrictStr | None = None
    VolumeType: StrictStr | None = None
    VolumeSizeInBytes: StrictInt | None = None
    VolumeAttachmentStatus: StrictStr | None = None
