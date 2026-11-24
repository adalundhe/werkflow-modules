from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .storage_gateway_volume_info import StorageGatewayVolumeInfo


class StorageGatewayListVolumesResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    Marker: StrictStr | None = None
    VolumeInfos: list[StorageGatewayVolumeInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
