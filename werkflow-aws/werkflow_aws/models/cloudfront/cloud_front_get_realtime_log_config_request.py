from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetRealtimeLogConfigRequest(BaseModel):
    Name: StrictStr | None = None
    ARN: StrictStr | None = None
