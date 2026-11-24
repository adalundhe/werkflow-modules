from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2TerminateClientVpnConnectionsRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    ConnectionId: StrictStr | None = None
    Username: StrictStr | None = None
    DryRun: StrictBool | None = None
