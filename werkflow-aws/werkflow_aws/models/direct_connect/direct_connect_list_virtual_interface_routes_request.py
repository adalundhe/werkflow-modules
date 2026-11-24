from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .direct_connect_route_filters import DirectConnectRouteFilters


class DirectConnectListVirtualInterfaceRoutesRequest(BaseModel):
    virtualInterfaceId: StrictStr | None = None
    filters: DirectConnectRouteFilters | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
