from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_bgp_options import NetworkManagerBgpOptions
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateConnectPeerRequest(BaseModel):
    ConnectAttachmentId: StrictStr
    PeerAddress: StrictStr
    CoreNetworkAddress: StrictStr | None = None
    BgpOptions: NetworkManagerBgpOptions | None = None
    InsideCidrBlocks: list[StrictStr] | None = None
    Tags: list[NetworkManagerTag] | None = None
    ClientToken: StrictStr | None = None
    SubnetArn: StrictStr | None = None
