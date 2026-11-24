from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieUpdateResourceProfileRequest(BaseModel):
    resourceArn: StrictStr
    sensitivityScoreOverride: StrictInt | None = None
