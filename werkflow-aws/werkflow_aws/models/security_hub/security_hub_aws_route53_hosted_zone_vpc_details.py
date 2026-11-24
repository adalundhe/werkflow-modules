from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRoute53HostedZoneVpcDetails(BaseModel):
    Id: StrictStr | None = None
    Region: StrictStr | None = None
