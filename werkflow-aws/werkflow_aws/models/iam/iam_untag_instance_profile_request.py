from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagInstanceProfileRequest(BaseModel):
    InstanceProfileName: StrictStr
    TagKeys: list[StrictStr]
