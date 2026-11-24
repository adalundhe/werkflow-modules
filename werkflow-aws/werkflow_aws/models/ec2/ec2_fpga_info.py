from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ec2_fpga_device_info import EC2FpgaDeviceInfo


class EC2FpgaInfo(BaseModel):
    Fpgas: list[EC2FpgaDeviceInfo] | None = None
    TotalFpgaMemoryInMiB: StrictInt | None = None
