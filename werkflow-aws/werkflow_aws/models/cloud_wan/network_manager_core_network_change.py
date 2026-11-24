from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_core_network_change_values import NetworkManagerCoreNetworkChangeValues


class NetworkManagerCoreNetworkChange(BaseModel):
    Type: StrictStr | None = None
    Action: StrictStr | None = None
    Identifier: StrictStr | None = None
    PreviousValues: NetworkManagerCoreNetworkChangeValues | None = None
    NewValues: NetworkManagerCoreNetworkChangeValues | None = None
    IdentifierPath: StrictStr | None = None
