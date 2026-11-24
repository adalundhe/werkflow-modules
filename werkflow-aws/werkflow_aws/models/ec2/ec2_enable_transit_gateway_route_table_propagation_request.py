from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableTransitGatewayRouteTablePropagationRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    TransitGatewayAttachmentId: StrictStr | None = None
    DryRun: StrictBool | None = None
    TransitGatewayRouteTableAnnouncementId: StrictStr | None = None
