from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCoreNetworkSummary(BaseModel):
    CoreNetworkId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    GlobalNetworkId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    State: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
