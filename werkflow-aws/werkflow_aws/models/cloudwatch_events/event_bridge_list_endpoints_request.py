from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListEndpointsRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    HomeRegion: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
