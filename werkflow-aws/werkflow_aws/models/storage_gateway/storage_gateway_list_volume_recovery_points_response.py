from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_volume_recovery_point_info import StorageGatewayVolumeRecoveryPointInfo


class StorageGatewayListVolumeRecoveryPointsResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    VolumeRecoveryPointInfos: list[StorageGatewayVolumeRecoveryPointInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
