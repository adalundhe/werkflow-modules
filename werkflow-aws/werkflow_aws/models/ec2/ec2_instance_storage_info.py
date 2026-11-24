from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_disk_info import EC2DiskInfo


class EC2InstanceStorageInfo(BaseModel):
    TotalSizeInGB: StrictInt | None = None
    Disks: list[EC2DiskInfo] | None = None
    NvmeSupport: StrictStr | None = None
    EncryptionSupport: StrictStr | None = None
