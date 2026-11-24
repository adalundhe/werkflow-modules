from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .emr_ebs_block_device_config import EMREbsBlockDeviceConfig


class EMREbsConfiguration(BaseModel):
    EbsBlockDeviceConfigs: list[EMREbsBlockDeviceConfig] | None = None
    EbsOptimized: StrictBool | None = None
