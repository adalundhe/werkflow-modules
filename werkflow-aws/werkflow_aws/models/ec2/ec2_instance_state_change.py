from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_instance_state import EC2InstanceState


class EC2InstanceStateChange(BaseModel):
    CurrentState: EC2InstanceState | None = None
    InstanceId: StrictStr | None = None
    PreviousState: EC2InstanceState | None = None
