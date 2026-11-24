from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ec2_gpu_device_info import EC2GpuDeviceInfo


class EC2GpuInfo(BaseModel):
    Gpus: list[EC2GpuDeviceInfo] | None = None
    TotalGpuMemoryInMiB: StrictInt | None = None
