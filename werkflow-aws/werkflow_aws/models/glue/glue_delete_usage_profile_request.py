from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteUsageProfileRequest(BaseModel):
    Name: StrictStr
