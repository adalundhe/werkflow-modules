from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTransitGatewayRouteTableAnnouncementRequest(BaseModel):
    TransitGatewayRouteTableAnnouncementId: StrictStr
    DryRun: StrictBool | None = None
