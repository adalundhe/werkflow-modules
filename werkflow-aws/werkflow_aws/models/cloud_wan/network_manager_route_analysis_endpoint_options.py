from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRouteAnalysisEndpointOptions(BaseModel):
    TransitGatewayAttachmentArn: StrictStr | None = None
    TransitGatewayArn: StrictStr | None = None
    IpAddress: StrictStr | None = None
