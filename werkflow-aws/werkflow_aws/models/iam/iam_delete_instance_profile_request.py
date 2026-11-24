from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteInstanceProfileRequest(BaseModel):
    InstanceProfileName: StrictStr
