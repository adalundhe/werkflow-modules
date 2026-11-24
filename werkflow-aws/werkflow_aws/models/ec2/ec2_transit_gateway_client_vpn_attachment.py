from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayClientVpnAttachment(BaseModel):
    TransitGatewayAttachmentId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
    ClientVpnEndpointId: StrictStr | None = None
    ClientVpnOwnerId: StrictStr | None = None
    State: StrictStr | None = None
    CreationTime: StrictStr | None = None
