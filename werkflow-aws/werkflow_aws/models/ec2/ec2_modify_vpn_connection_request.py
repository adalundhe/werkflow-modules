from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpnConnectionRequest(BaseModel):
    VpnConnectionId: StrictStr
    TransitGatewayId: StrictStr | None = None
    CustomerGatewayId: StrictStr | None = None
    VpnGatewayId: StrictStr | None = None
    DryRun: StrictBool | None = None
