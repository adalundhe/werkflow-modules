from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    PolicyRevisionId: StrictStr | None = None
