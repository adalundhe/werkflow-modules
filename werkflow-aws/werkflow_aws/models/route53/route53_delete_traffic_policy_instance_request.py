from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DeleteTrafficPolicyInstanceRequest(BaseModel):
    Id: StrictStr
