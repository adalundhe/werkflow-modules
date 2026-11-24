from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeEndpointRequest(BaseModel):
    Name: StrictStr
    HomeRegion: StrictStr | None = None
