from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerConnectPeerSummary(BaseModel):
    CoreNetworkId: StrictStr | None = None
    ConnectAttachmentId: StrictStr | None = None
    ConnectPeerId: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
    ConnectPeerState: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
    SubnetArn: StrictStr | None = None
