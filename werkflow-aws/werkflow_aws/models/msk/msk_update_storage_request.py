from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_provisioned_throughput import MSKProvisionedThroughput


class MSKUpdateStorageRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    ProvisionedThroughput: MSKProvisionedThroughput | None = None
    StorageMode: Literal['LOCAL', 'TIERED'] | None = None
    VolumeSizeGB: StrictInt | None = None
