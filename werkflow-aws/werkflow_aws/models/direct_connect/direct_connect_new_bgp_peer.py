from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectNewBGPPeer(BaseModel):
    asn: StrictInt | None = None
    asnLong: StrictInt | None = None
    authKey: StrictStr | None = None
    addressFamily: Literal['ipv4', 'ipv6'] | None = None
    amazonAddress: StrictStr | None = None
    customerAddress: StrictStr | None = None
