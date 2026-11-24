from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_host_path import GuardDutyHostPath


class GuardDutyVolume(BaseModel):
    Name: StrictStr | None = None
    HostPath: GuardDutyHostPath | None = None
