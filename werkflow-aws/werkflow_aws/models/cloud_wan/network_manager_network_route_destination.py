from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerNetworkRouteDestination(BaseModel):
    CoreNetworkAttachmentId: StrictStr | None = None
    TransitGatewayAttachmentId: StrictStr | None = None
    SegmentName: StrictStr | None = None
    NetworkFunctionGroupName: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
