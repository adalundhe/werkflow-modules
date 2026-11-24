from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubVpcInfoPeeringOptionsDetails(BaseModel):
    AllowDnsResolutionFromRemoteVpc: StrictBool | None = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: StrictBool | None = None
    AllowEgressFromLocalVpcToRemoteClassicLink: StrictBool | None = None
