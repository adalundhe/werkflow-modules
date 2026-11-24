from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeStorediSCSIVolumesRequest(BaseModel):
    VolumeARNs: list[StrictStr]
