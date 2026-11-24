from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53DeleteTrafficPolicyRequest(BaseModel):
    Id: StrictStr
    Version: StrictInt
