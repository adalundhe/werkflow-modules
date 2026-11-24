from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_port_range import SecurityHubPortRange


class SecurityHubNetwork(BaseModel):
    Direction: StrictStr | None = None
    Protocol: StrictStr | None = None
    OpenPortRange: SecurityHubPortRange | None = None
    SourceIpV4: StrictStr | None = None
    SourceIpV6: StrictStr | None = None
    SourcePort: StrictInt | None = None
    SourceDomain: StrictStr | None = None
    SourceMac: StrictStr | None = None
    DestinationIpV4: StrictStr | None = None
    DestinationIpV6: StrictStr | None = None
    DestinationPort: StrictInt | None = None
    DestinationDomain: StrictStr | None = None
