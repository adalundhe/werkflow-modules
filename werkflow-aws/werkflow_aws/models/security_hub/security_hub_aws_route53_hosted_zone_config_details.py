from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRoute53HostedZoneConfigDetails(BaseModel):
    Comment: StrictStr | None = None
