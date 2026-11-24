from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CidrAuthorizationContext(BaseModel):
    Message: StrictStr
    Signature: StrictStr
