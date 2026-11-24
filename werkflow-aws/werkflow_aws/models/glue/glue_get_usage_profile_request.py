from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetUsageProfileRequest(BaseModel):
    Name: StrictStr
