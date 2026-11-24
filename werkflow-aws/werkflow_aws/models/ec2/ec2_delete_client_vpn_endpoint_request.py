from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteClientVpnEndpointRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    DryRun: StrictBool | None = None
