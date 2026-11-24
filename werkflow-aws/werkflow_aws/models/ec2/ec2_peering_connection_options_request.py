from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2PeeringConnectionOptionsRequest(BaseModel):
    AllowDnsResolutionFromRemoteVpc: StrictBool | None = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: StrictBool | None = None
    AllowEgressFromLocalVpcToRemoteClassicLink: StrictBool | None = None
    AllowMultipathResilience: StrictBool | None = None
    MultipathResilienceMode: Literal['always-on'] | None = None
