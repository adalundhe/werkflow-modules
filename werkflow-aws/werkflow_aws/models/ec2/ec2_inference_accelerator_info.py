from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ec2_inference_device_info import EC2InferenceDeviceInfo


class EC2InferenceAcceleratorInfo(BaseModel):
    Accelerators: list[EC2InferenceDeviceInfo] | None = None
    TotalInferenceMemoryInMiB: StrictInt | None = None
