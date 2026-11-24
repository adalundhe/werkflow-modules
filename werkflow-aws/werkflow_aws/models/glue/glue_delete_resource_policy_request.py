from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteResourcePolicyRequest(BaseModel):
    PolicyHashCondition: StrictStr | None = None
    ResourceArn: StrictStr | None = None
