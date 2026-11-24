from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .network_manager_network_resource_summary import NetworkManagerNetworkResourceSummary


class NetworkManagerPathComponent(BaseModel):
    Sequence: StrictInt | None = None
    Resource: NetworkManagerNetworkResourceSummary | None = None
    DestinationCidrBlock: StrictStr | None = None
