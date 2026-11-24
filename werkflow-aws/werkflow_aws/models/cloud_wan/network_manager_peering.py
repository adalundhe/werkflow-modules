from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .network_manager_peering_error import NetworkManagerPeeringError
from .network_manager_tag import NetworkManagerTag


class NetworkManagerPeering(BaseModel):
    CoreNetworkId: StrictStr | None = None
    CoreNetworkArn: StrictStr | None = None
    PeeringId: StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    PeeringType: StrictStr | None = None
    State: StrictStr | None = None
    EdgeLocation: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    Tags: list[NetworkManagerTag] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastModificationErrors: list[NetworkManagerPeeringError] | None = None
