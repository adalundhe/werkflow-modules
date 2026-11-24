from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .organizations_policy_type import OrganizationsPolicyType


class OrganizationsListPoliciesRequest(BaseModel):
    Filter: OrganizationsPolicyType | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
