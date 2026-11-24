from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .auto_scaling_ebs import AutoScalingEbs


class AutoScalingBlockDeviceMapping(BaseModel):
    VirtualName: StrictStr | None = None
    DeviceName: StrictStr | None = None
    Ebs: AutoScalingEbs | None = None
    NoDevice: StrictBool | None = None
