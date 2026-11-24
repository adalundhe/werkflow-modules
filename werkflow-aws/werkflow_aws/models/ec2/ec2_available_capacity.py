from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ec2_instance_capacity import EC2InstanceCapacity


class EC2AvailableCapacity(BaseModel):
    AvailableInstanceCapacity: list[EC2InstanceCapacity] | None = None
    AvailableVCpus: StrictInt | None = None
