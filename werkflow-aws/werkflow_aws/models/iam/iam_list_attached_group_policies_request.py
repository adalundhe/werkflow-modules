from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListAttachedGroupPoliciesRequest(BaseModel):
    GroupName: StrictStr
    PathPrefix: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
