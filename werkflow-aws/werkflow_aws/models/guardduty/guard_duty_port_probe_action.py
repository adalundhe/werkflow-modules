from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .guard_duty_port_probe_detail import GuardDutyPortProbeDetail


class GuardDutyPortProbeAction(BaseModel):
    Blocked: StrictBool | None = None
    PortProbeDetails: list[GuardDutyPortProbeDetail] | None = None
