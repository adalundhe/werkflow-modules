from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsAttachPolicyRequest(BaseModel):
    PolicyId: StrictStr
    TargetId: StrictStr
