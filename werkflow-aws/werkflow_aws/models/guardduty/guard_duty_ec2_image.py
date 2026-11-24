from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEc2Image(BaseModel):
    Ec2InstanceUids: list[StrictStr] | None = None
