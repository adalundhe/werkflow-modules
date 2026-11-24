from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ec2_media_device_info import EC2MediaDeviceInfo


class EC2MediaAcceleratorInfo(BaseModel):
    Accelerators: list[EC2MediaDeviceInfo] | None = None
    TotalMediaMemoryInMiB: StrictInt | None = None
