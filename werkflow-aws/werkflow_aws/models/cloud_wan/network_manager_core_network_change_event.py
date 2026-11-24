from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_change_event_values import NetworkManagerCoreNetworkChangeEventValues


class NetworkManagerCoreNetworkChangeEvent(BaseModel):
    Type: StrictStr | None = None
    Action: StrictStr | None = None
    IdentifierPath: StrictStr | None = None
    EventTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Values: NetworkManagerCoreNetworkChangeEventValues | None = None
