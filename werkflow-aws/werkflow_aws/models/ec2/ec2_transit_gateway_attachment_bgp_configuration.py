from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TransitGatewayAttachmentBgpConfiguration(BaseModel):
    TransitGatewayAsn: StrictInt | None = None
    PeerAsn: StrictInt | None = None
    TransitGatewayAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
    BgpStatus: StrictStr | None = None
