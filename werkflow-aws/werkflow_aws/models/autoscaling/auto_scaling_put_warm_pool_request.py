from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_instance_reuse_policy import AutoScalingInstanceReusePolicy


class AutoScalingPutWarmPoolRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    MaxGroupPreparedCapacity: StrictInt | None = None
    MinSize: StrictInt | None = None
    PoolState: Literal['Stopped', 'Running', 'Hibernated'] | None = None
    InstanceReusePolicy: AutoScalingInstanceReusePolicy | None = None
