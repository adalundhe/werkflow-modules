from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_connect_peer import NetworkManagerConnectPeer


class NetworkManagerDeleteConnectPeerResponse(BaseModel):
    ConnectPeer: NetworkManagerConnectPeer | None = None
    ResponseMetadata: dict[str, Any] | None = None
