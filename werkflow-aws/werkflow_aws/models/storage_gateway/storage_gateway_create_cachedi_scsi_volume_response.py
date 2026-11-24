from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayCreateCachediSCSIVolumeResponse(BaseModel):
    VolumeARN: StrictStr | None = None
    TargetARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
