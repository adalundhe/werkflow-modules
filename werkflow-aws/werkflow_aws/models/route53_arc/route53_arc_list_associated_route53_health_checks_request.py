from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53ARCListAssociatedRoute53HealthChecksRequest(BaseModel):
    RoutingControlArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
