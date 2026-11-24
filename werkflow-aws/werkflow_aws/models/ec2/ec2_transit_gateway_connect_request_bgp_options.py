from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2TransitGatewayConnectRequestBgpOptions(BaseModel):
    PeerAsn: StrictInt | None = None
