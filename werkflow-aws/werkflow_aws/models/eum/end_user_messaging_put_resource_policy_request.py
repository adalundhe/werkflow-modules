from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    Policy: StrictStr
