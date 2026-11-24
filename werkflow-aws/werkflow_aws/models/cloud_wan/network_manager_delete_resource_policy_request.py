from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
