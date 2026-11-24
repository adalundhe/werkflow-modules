from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyClientVpnEndpointAuthorizationPolicyRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    PolicyDocument: StrictStr | None = None
    Description: StrictStr | None = None
    ShadowMode: Literal['enabled', 'disabled'] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
