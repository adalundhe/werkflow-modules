from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_cachedi_scsi_volume import StorageGatewayCachediSCSIVolume


class StorageGatewayDescribeCachediSCSIVolumesResponse(BaseModel):
    CachediSCSIVolumes: list[StorageGatewayCachediSCSIVolume] | None = None
    ResponseMetadata: dict[str, Any] | None = None
