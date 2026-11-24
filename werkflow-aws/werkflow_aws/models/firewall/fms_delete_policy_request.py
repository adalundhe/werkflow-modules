from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSDeletePolicyRequest(BaseModel):
    PolicyId: StrictStr
    DeleteAllPolicyResources: StrictBool | None = None
