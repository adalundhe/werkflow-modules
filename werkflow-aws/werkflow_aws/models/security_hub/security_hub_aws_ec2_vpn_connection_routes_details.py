from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2VpnConnectionRoutesDetails(BaseModel):
    DestinationCidrBlock: StrictStr | None = None
    State: StrictStr | None = None
