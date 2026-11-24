from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetRolePolicyResponse(BaseModel):
    RoleName: StrictStr | None = None
    PolicyName: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
