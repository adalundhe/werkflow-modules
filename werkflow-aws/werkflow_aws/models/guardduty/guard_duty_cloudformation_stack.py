from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCloudformationStack(BaseModel):
    Ec2InstanceUids: list[StrictStr] | None = None
