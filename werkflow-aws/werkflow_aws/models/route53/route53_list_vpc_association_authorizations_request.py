from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListVPCAssociationAuthorizationsRequest(BaseModel):
    HostedZoneId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictStr | None = None
