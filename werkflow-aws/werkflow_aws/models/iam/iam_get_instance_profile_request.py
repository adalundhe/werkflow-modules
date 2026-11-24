from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetInstanceProfileRequest(BaseModel):
    InstanceProfileName: StrictStr
