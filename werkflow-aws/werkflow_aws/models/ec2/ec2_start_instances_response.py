from __future__ import annotations
from pydantic import BaseModel
from .ec2_instance_state_change import EC2InstanceStateChange


class EC2StartInstancesResponse(BaseModel):
    StartingInstances: list[EC2InstanceStateChange] | None = None
