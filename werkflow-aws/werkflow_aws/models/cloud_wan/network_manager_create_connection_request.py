from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateConnectionRequest(BaseModel):
    GlobalNetworkId: StrictStr
    DeviceId: StrictStr
    ConnectedDeviceId: StrictStr
    LinkId: StrictStr | None = None
    ConnectedLinkId: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
