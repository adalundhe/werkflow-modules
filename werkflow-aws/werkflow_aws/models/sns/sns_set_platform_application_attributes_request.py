from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSetPlatformApplicationAttributesRequest(BaseModel):
    PlatformApplicationArn: StrictStr
    Attributes: dict[StrictStr, StrictStr]
