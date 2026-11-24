from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VpcPeeringConnectionOptionsDescription(BaseModel):
    AllowDnsResolutionFromRemoteVpc: StrictBool | None = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: StrictBool | None = None
    AllowEgressFromLocalVpcToRemoteClassicLink: StrictBool | None = None
    AllowMultipathResilience: StrictBool | None = None
    MultipathResilienceMode: StrictStr | None = None
