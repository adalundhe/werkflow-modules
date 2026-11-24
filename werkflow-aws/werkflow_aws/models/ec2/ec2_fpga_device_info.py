from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_fpga_device_memory_info import EC2FpgaDeviceMemoryInfo


class EC2FpgaDeviceInfo(BaseModel):
    Name: StrictStr | None = None
    Manufacturer: StrictStr | None = None
    Count: StrictInt | None = None
    MemoryInfo: EC2FpgaDeviceMemoryInfo | None = None
