from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableTransitGatewayRouteTablePropagationRequest(BaseModel):
    TransitGatewayRouteTableId: StrictStr
    TransitGatewayAttachmentId: StrictStr | None = None
    DryRun: StrictBool | None = None
    TransitGatewayRouteTableAnnouncementId: StrictStr | None = None
