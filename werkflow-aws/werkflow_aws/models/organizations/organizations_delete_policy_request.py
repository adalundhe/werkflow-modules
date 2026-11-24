from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDeletePolicyRequest(BaseModel):
    PolicyId: StrictStr
