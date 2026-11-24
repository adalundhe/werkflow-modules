from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    ResourcePolicy: StrictStr
    PolicyRevisionId: StrictStr | None = None
