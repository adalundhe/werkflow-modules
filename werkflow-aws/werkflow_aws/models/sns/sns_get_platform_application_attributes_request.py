from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSGetPlatformApplicationAttributesRequest(BaseModel):
    PlatformApplicationArn: StrictStr
