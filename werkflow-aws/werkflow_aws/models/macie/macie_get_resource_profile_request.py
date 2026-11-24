from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetResourceProfileRequest(BaseModel):
    resourceArn: StrictStr
