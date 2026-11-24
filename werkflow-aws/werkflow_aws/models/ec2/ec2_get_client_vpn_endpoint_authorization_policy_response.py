from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2GetClientVpnEndpointAuthorizationPolicyResponse(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    Description: StrictStr | None = None
    ShadowMode: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
