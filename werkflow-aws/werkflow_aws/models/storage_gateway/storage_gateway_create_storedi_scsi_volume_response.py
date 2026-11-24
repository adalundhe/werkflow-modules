from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayCreateStorediSCSIVolumeResponse(BaseModel):
    VolumeARN: StrictStr | None = None
    VolumeSizeInBytes: StrictInt | None = None
    TargetARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
