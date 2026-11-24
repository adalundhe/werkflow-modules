from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateSnapshotFromVolumeRecoveryPointRequest(BaseModel):
    VolumeARN: StrictStr
    SnapshotDescription: StrictStr
    Tags: list[StorageGatewayTag] | None = None
