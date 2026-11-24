from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_gpu_device_memory_info import EC2GpuDeviceMemoryInfo


class EC2GpuDeviceInfo(BaseModel):
    Name: StrictStr | None = None
    Manufacturer: StrictStr | None = None
    Count: StrictInt | None = None
    LogicalGpuCount: StrictInt | None = None
    GpuPartitionSize: StrictFloat | StrictInt | None = None
    Workloads: list[StrictStr] | None = None
    MemoryInfo: EC2GpuDeviceMemoryInfo | None = None
