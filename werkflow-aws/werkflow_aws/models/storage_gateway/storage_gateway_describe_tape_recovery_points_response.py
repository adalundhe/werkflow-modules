from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_tape_recovery_point_info import StorageGatewayTapeRecoveryPointInfo


class StorageGatewayDescribeTapeRecoveryPointsResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    TapeRecoveryPointInfos: list[StorageGatewayTapeRecoveryPointInfo] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
