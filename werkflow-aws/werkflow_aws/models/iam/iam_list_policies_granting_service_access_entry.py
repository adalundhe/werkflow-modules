from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_policy_granting_service_access import IAMPolicyGrantingServiceAccess


class IAMListPoliciesGrantingServiceAccessEntry(BaseModel):
    ServiceNamespace: StrictStr | None = None
    Policies: list[IAMPolicyGrantingServiceAccess] | None = None
