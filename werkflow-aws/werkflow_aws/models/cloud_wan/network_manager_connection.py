from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerConnection(BaseModel):
    ConnectionId: StrictStr | None = None
    ConnectionArn: StrictStr | None = None
    GlobalNetworkId: StrictStr | None = None
    DeviceId: StrictStr | None = None
    ConnectedDeviceId: StrictStr | None = None
    LinkId: StrictStr | None = None
    ConnectedLinkId: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
