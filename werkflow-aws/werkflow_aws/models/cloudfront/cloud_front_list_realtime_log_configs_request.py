from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListRealtimeLogConfigsRequest(BaseModel):
    MaxItems: StrictStr | None = None
    Marker: StrictStr | None = None
