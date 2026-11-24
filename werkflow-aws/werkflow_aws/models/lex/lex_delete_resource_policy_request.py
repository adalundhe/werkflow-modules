from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
    expectedRevisionId: StrictStr | None = None
