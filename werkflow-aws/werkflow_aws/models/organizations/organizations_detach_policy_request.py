from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDetachPolicyRequest(BaseModel):
    PolicyId: StrictStr
    TargetId: StrictStr
