from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerPutResourcePolicyRequest(BaseModel):
    PolicyDocument: StrictStr
    ResourceArn: StrictStr
