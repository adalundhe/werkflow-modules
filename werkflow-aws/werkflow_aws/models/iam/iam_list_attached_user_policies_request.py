from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListAttachedUserPoliciesRequest(BaseModel):
    UserName: StrictStr
    PathPrefix: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
