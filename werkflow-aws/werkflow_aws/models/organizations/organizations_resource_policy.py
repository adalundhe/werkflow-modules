from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_resource_policy_summary import OrganizationsResourcePolicySummary


class OrganizationsResourcePolicy(BaseModel):
    ResourcePolicySummary: OrganizationsResourcePolicySummary | None = None
    Content: StrictStr | None = None
