from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SetProjectPoliciesRequest(BaseModel):
    policyIds: list[StrictStr] | None = None
