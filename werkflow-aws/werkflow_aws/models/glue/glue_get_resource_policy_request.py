from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr | None = None
