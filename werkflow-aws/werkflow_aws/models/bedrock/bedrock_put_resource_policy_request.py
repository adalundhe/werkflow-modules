from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockPutResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
    resourcePolicy: StrictStr
