from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListAttachedRolePoliciesRequest(BaseModel):
    RoleName: StrictStr
    PathPrefix: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
