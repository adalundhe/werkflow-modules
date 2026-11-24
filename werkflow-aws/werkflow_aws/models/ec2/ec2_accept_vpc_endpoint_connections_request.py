from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AcceptVpcEndpointConnectionsRequest(BaseModel):
    ServiceId: StrictStr
    VpcEndpointIds: list[StrictStr]
    DryRun: StrictBool | None = None
    TransitGatewayAttachmentIds: list[StrictStr] | None = None
