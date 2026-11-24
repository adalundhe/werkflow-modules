from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_policy_version import IAMPolicyVersion


class IAMListPolicyVersionsResponse(BaseModel):
    Versions: list[IAMPolicyVersion] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
