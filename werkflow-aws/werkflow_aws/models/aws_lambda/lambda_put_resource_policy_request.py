from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    Policy: StrictStr
    RevisionId: StrictStr | None = None
