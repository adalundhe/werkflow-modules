from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    RevisionId: StrictStr | None = None
