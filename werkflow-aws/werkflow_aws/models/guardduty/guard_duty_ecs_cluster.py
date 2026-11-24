from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEcsCluster(BaseModel):
    Status: StrictStr | None = None
    Ec2InstanceUids: list[StrictStr] | None = None
