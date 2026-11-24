from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_connect_peer_association import NetworkManagerConnectPeerAssociation


class NetworkManagerDisassociateConnectPeerResponse(BaseModel):
    ConnectPeerAssociation: NetworkManagerConnectPeerAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
