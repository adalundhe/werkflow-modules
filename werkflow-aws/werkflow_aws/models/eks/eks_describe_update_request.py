from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDescribeUpdateRequest(BaseModel):
    name: StrictStr
    updateId: StrictStr
    nodegroupName: StrictStr | None = None
    addonName: StrictStr | None = None
    capabilityName: StrictStr | None = None
