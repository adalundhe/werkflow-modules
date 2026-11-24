from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_inference_device_memory_info import EC2InferenceDeviceMemoryInfo


class EC2InferenceDeviceInfo(BaseModel):
    Count: StrictInt | None = None
    Name: StrictStr | None = None
    Manufacturer: StrictStr | None = None
    MemoryInfo: EC2InferenceDeviceMemoryInfo | None = None
