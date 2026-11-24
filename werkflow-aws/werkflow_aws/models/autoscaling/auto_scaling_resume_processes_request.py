from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingResumeProcessesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ScalingProcesses: list[StrictStr] | None = None
