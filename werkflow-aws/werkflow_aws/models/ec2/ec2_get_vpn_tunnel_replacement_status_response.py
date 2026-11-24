from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_maintenance_details import EC2MaintenanceDetails


class EC2GetVpnTunnelReplacementStatusResponse(BaseModel):
    VpnConnectionId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    CustomerGatewayId: StrictStr | None = None
    VpnGatewayId: StrictStr | None = None
    VpnTunnelOutsideIpAddress: StrictStr | None = None
    MaintenanceDetails: EC2MaintenanceDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
