from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontListDistributionsByRealtimeLogConfigRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    RealtimeLogConfigName: StrictStr | None = None
    RealtimeLogConfigArn: StrictStr | None = None
