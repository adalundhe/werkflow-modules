from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
