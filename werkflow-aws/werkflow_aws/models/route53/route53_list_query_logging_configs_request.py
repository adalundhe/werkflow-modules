from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListQueryLoggingConfigsRequest(BaseModel):
    HostedZoneId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictStr | None = None
