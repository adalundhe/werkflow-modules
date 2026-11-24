from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingLaunchInstancesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    RequestedCapacity: StrictInt
    ClientToken: StrictStr
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    SubnetIds: list[StrictStr] | None = None
    RetryStrategy: Literal['retry-with-group-configuration', 'none'] | None = None
