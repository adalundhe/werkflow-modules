from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .msk_provisioned_throughput import MSKProvisionedThroughput


class MSKEBSStorageInfoModel(BaseModel):
    ProvisionedThroughput: MSKProvisionedThroughput | None = None
    VolumeSize: StrictInt | None = None
