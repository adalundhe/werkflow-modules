from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteInstanceProfileRequest(BaseModel):
    InstanceProfileIdentifier: StrictStr
