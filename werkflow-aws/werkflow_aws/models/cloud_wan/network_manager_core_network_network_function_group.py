from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_service_insertion_segments import NetworkManagerServiceInsertionSegments


class NetworkManagerCoreNetworkNetworkFunctionGroup(BaseModel):
    Name: StrictStr | None = None
    EdgeLocations: list[StrictStr] | None = None
    Segments: NetworkManagerServiceInsertionSegments | None = None
