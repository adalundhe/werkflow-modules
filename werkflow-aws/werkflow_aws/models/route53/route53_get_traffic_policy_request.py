from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53GetTrafficPolicyRequest(BaseModel):
    Id: StrictStr
    Version: StrictInt
