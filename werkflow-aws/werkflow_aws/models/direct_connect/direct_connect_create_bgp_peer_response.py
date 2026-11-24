from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_virtual_interface import DirectConnectVirtualInterface


class DirectConnectCreateBGPPeerResponse(BaseModel):
    virtualInterface: DirectConnectVirtualInterface | None = None
    ResponseMetadata: dict[str, Any] | None = None
