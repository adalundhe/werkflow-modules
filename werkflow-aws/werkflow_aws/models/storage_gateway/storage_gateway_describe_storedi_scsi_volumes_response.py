from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .storage_gateway_storedi_scsi_volume import StorageGatewayStorediSCSIVolume


class StorageGatewayDescribeStorediSCSIVolumesResponse(BaseModel):
    StorediSCSIVolumes: list[StorageGatewayStorediSCSIVolume] | None = None
    ResponseMetadata: dict[str, Any] | None = None
