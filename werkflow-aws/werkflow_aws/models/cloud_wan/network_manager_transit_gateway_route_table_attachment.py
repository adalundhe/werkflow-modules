from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_attachment import NetworkManagerAttachment


class NetworkManagerTransitGatewayRouteTableAttachment(BaseModel):
    Attachment: NetworkManagerAttachment | None = None
    PeeringId: StrictStr | None = None
    TransitGatewayRouteTableArn: StrictStr | None = None
