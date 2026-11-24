from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRouteAnalysisEndpointOptionsSpecification(BaseModel):
    TransitGatewayAttachmentArn: StrictStr | None = None
    IpAddress: StrictStr | None = None
