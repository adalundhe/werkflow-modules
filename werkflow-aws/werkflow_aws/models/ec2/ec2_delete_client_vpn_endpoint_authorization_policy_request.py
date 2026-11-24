from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteClientVpnEndpointAuthorizationPolicyRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    DryRun: StrictBool | None = None
