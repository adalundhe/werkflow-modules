from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2RouteServerBgpOptionsRequest(BaseModel):
    PeerAsn: StrictInt
    PeerLivenessDetection: Literal['bfd', 'bgp-keepalive'] | None = None
