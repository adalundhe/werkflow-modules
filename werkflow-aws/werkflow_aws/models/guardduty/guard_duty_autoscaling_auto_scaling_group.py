from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAutoscalingAutoScalingGroup(BaseModel):
    Ec2InstanceUids: list[StrictStr] | None = None
