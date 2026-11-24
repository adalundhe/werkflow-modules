from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayAttachmentPropagation(BaseModel):
    TransitGatewayRouteTableId: StrictStr | None = None
    State: StrictStr | None = None
