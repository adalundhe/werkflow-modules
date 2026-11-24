from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_network_autonomous_system import SecurityHubNetworkAutonomousSystem
from .security_hub_network_connection import SecurityHubNetworkConnection
from .security_hub_network_geo_location import SecurityHubNetworkGeoLocation


class SecurityHubNetworkEndpoint(BaseModel):
    Id: StrictStr | None = None
    Ip: StrictStr | None = None
    Domain: StrictStr | None = None
    Port: StrictInt | None = None
    Location: SecurityHubNetworkGeoLocation | None = None
    AutonomousSystem: SecurityHubNetworkAutonomousSystem | None = None
    Connection: SecurityHubNetworkConnection | None = None
