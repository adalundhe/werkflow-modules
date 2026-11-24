from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingSuspendProcessesRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ScalingProcesses: list[StrictStr] | None = None
