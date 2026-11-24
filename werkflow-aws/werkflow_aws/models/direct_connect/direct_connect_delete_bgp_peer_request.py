from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectDeleteBGPPeerRequest(BaseModel):
    virtualInterfaceId: StrictStr | None = None
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    customerAddress: StrictStr | None = None
    bgpPeerId: StrictStr | None = None
