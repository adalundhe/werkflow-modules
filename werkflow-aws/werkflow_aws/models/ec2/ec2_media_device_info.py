from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_media_device_memory_info import EC2MediaDeviceMemoryInfo


class EC2MediaDeviceInfo(BaseModel):
    Count: StrictInt | None = None
    Name: StrictStr | None = None
    Manufacturer: StrictStr | None = None
    MemoryInfo: EC2MediaDeviceMemoryInfo | None = None
