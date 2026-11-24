from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEc2LaunchTemplate(BaseModel):
    Ec2InstanceUids: list[StrictStr] | None = None
    Version: StrictStr | None = None
