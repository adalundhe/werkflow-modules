from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2StartVpcEndpointServicePrivateDnsVerificationRequest(BaseModel):
    ServiceId: StrictStr
    DryRun: StrictBool | None = None
