from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CreateTrafficPolicyVersionRequest(BaseModel):
    Id: StrictStr
    Document: StrictStr
    Comment: StrictStr | None = None
