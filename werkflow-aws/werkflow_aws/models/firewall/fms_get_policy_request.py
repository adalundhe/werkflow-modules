from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSGetPolicyRequest(BaseModel):
    PolicyId: StrictStr
