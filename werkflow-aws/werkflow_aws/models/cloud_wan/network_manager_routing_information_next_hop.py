from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRoutingInformationNextHop(BaseModel):
    IpAddress: StrictStr | None = None
    CoreNetworkAttachmentId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    SegmentName: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
