from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_connect_peer_configuration import NetworkManagerConnectPeerConfiguration
from .network_manager_connect_peer_error import NetworkManagerConnectPeerError
from .network_manager_tag import NetworkManagerTag


class NetworkManagerConnectPeer(BaseModel):
    CoreNetworkId: StrictStr | None = None
    ConnectAttachmentId: StrictStr | None = None
    ConnectPeerId: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
    State: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Configuration: NetworkManagerConnectPeerConfiguration | None = None
    Tags: list[NetworkManagerTag] | None = None
    SubnetArn: StrictStr | None = None
    LastModificationErrors: list[NetworkManagerConnectPeerError] | None = None
