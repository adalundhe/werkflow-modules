from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_policy import IAMPolicy


class IAMListPoliciesResponse(BaseModel):
    Policies: list[IAMPolicy] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
