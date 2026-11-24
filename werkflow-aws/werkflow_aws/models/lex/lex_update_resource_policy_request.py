from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexUpdateResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
    policy: StrictStr
    expectedRevisionId: StrictStr | None = None
