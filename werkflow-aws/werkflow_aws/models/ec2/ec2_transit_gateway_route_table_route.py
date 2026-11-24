from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayRouteTableRoute(BaseModel):
    DestinationCidr: StrictStr | None = None
    State: StrictStr | None = None
    RouteOrigin: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
