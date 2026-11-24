from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyNetworkPorts(BaseModel):
    TargetPort: StrictStr | None = None
    RemotePort: StrictStr | None = None
    ResolverPort: StrictStr | None = None
    Ports: StrictStr | None = None
    PortsUsed: StrictStr | None = None
    PortCount: StrictInt | None = None
