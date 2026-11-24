from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsUpdatePolicyRequest(BaseModel):
    PolicyId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Content: StrictStr | None = None
