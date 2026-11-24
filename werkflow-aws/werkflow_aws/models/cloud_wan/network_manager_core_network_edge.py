from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerCoreNetworkEdge(BaseModel):
    EdgeLocation: StrictStr | None = None
    Asn: StrictInt | None = None
    InsideCidrBlocks: list[StrictStr] | None = None
