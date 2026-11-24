from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_policy_summary import OrganizationsPolicySummary


class OrganizationsListPoliciesResponse(BaseModel):
    Policies: list[OrganizationsPolicySummary] | None = None
    NextToken: StrictStr | None = None
