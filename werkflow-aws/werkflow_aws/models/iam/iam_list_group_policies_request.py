from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListGroupPoliciesRequest(BaseModel):
    GroupName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
