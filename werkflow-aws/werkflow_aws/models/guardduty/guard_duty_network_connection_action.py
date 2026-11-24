from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .guard_duty_local_ip_details import GuardDutyLocalIpDetails
from .guard_duty_local_port_details import GuardDutyLocalPortDetails
from .guard_duty_remote_ip_details import GuardDutyRemoteIpDetails
from .guard_duty_remote_port_details import GuardDutyRemotePortDetails


class GuardDutyNetworkConnectionAction(BaseModel):
    Blocked: StrictBool | None = None
    ConnectionDirection: StrictStr | None = None
    LocalPortDetails: GuardDutyLocalPortDetails | None = None
    Protocol: StrictStr | None = None
    LocalIpDetails: GuardDutyLocalIpDetails | None = None
    LocalNetworkInterface: StrictStr | None = None
    RemoteIpDetails: GuardDutyRemoteIpDetails | None = None
    RemotePortDetails: GuardDutyRemotePortDetails | None = None
