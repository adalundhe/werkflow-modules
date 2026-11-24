from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_attached_policy import IAMAttachedPolicy


class IAMListAttachedRolePoliciesResponse(BaseModel):
    AttachedPolicies: list[IAMAttachedPolicy] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
