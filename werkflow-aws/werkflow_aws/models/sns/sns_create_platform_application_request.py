from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSCreatePlatformApplicationRequest(BaseModel):
    Name: StrictStr
    Platform: StrictStr
    Attributes: dict[StrictStr, StrictStr]
