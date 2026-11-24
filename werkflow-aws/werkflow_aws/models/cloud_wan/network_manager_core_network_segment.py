from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerCoreNetworkSegment(BaseModel):
    Name: StrictStr | None = None
    EdgeLocations: list[StrictStr] | None = None
    SharedSegments: list[StrictStr] | None = None
