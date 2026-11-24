from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeCachediSCSIVolumesRequest(BaseModel):
    VolumeARNs: list[StrictStr]
