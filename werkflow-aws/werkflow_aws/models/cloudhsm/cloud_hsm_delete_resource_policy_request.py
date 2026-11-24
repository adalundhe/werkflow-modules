from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr | None = None
