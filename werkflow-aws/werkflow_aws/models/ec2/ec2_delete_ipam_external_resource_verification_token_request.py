from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamExternalResourceVerificationTokenRequest(BaseModel):
    IpamExternalResourceVerificationTokenId: StrictStr
    DryRun: StrictBool | None = None
