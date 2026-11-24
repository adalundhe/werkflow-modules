from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IAMListRolePoliciesResponse(BaseModel):
    PolicyNames: list[StrictStr] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
