from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyIamInstanceProfileV2(BaseModel):
    Ec2InstanceUids: list[StrictStr] | None = None
