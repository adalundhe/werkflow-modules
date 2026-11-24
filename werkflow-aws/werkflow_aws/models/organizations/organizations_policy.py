from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_policy_summary import OrganizationsPolicySummary


class OrganizationsPolicy(BaseModel):
    PolicySummary: OrganizationsPolicySummary | None = None
    Content: StrictStr | None = None
