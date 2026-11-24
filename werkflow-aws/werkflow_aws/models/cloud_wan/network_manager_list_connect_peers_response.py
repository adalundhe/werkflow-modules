from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_connect_peer_summary import NetworkManagerConnectPeerSummary


class NetworkManagerListConnectPeersResponse(BaseModel):
    ConnectPeers: list[NetworkManagerConnectPeerSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
