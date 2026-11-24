from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayDeleteResourcePolicyRequest(BaseModel):
    PolicyName: StrictStr
    PolicyRevisionId: StrictStr | None = None
