from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListTargetsForPolicyRequest(BaseModel):
    policyName: StrictStr
    marker: StrictStr | None = None
    pageSize: StrictInt | None = None
