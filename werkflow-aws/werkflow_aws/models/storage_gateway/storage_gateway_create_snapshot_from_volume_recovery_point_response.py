from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayCreateSnapshotFromVolumeRecoveryPointResponse(BaseModel):
    SnapshotId: StrictStr | None = None
    VolumeARN: StrictStr | None = None
    VolumeRecoveryPointTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
