from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .iam_policy_scope_type import IAMPolicyScopeType
from .iam_policy_usage_type import IAMPolicyUsageType


class IAMListPoliciesRequest(BaseModel):
    Scope: IAMPolicyScopeType | None = None
    OnlyAttached: StrictBool | None = None
    PathPrefix: StrictStr | None = None
    PolicyUsageFilter: IAMPolicyUsageType | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
