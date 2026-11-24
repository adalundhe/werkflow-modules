from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .auto_scaling_instance_reuse_policy import AutoScalingInstanceReusePolicy


class AutoScalingWarmPoolConfiguration(BaseModel):
    MaxGroupPreparedCapacity: StrictInt | None = None
    MinSize: StrictInt | None = None
    PoolState: StrictStr | None = None
    Status: StrictStr | None = None
    InstanceReusePolicy: AutoScalingInstanceReusePolicy | None = None
