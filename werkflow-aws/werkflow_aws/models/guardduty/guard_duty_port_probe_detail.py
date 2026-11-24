from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_local_ip_details import GuardDutyLocalIpDetails
from .guard_duty_local_port_details import GuardDutyLocalPortDetails
from .guard_duty_remote_ip_details import GuardDutyRemoteIpDetails


class GuardDutyPortProbeDetail(BaseModel):
    LocalPortDetails: GuardDutyLocalPortDetails | None = None
    LocalIpDetails: GuardDutyLocalIpDetails | None = None
    RemoteIpDetails: GuardDutyRemoteIpDetails | None = None
