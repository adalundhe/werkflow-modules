from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectBGPPeer(BaseModel):
    bgpPeerId: StrictStr | None = None
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    authKey: StrictStr | None = None
    addressFamily: StrictStr | None = None
    amazonAddress: StrictStr | None = None
    customerAddress: StrictStr | None = None
    bgpPeerState: StrictStr | None = None
    bgpStatus: StrictStr | None = None
    awsDeviceV2: StrictStr | None = None
    awsLogicalDeviceId: StrictStr | None = None
