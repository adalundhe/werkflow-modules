from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayListResourcePoliciesRequest(BaseModel):
    NextToken: StrictStr | None = None
