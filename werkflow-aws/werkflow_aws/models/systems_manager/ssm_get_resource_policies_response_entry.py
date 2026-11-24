from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetResourcePoliciesResponseEntry(BaseModel):
    PolicyId: StrictStr | None = None
    PolicyHash: StrictStr | None = None
    Policy: StrictStr | None = None
