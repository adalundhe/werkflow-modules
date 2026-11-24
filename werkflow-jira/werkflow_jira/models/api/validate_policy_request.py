from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ValidatePolicyRequest(BaseModel):
    policyIds: list[StrictStr] | None = None
