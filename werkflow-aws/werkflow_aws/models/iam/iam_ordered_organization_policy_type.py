from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMOrderedOrganizationPolicyType(BaseModel):
    ServiceControlPolicyInputList: list[StrictStr] | None = None
