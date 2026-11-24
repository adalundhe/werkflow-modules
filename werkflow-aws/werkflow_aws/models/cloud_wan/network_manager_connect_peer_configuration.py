from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_connect_peer_bgp_configuration import NetworkManagerConnectPeerBgpConfiguration


class NetworkManagerConnectPeerConfiguration(BaseModel):
    CoreNetworkAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
    InsideCidrBlocks: list[StrictStr] | None = None
    Protocol: StrictStr | None = None
    BgpConfigurations: list[NetworkManagerConnectPeerBgpConfiguration] | None = None
