from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CreateTrafficPolicyRequest(BaseModel):
    Name: StrictStr
    Document: StrictStr
    Comment: StrictStr | None = None
