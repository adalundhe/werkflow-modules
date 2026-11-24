from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_autonomous_system import GuardDutyAutonomousSystem
from .guard_duty_network_connection import GuardDutyNetworkConnection
from .guard_duty_network_geo_location import GuardDutyNetworkGeoLocation


class GuardDutyNetworkEndpoint(BaseModel):
    Id: StrictStr | None = None
    Ip: StrictStr | None = None
    Domain: StrictStr | None = None
    Port: StrictInt | None = None
    Location: GuardDutyNetworkGeoLocation | None = None
    AutonomousSystem: GuardDutyAutonomousSystem | None = None
    Connection: GuardDutyNetworkConnection | None = None
