from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_policy_summary_model import OrganizationsPolicySummaryModel


class OrganizationsPolicyModel(BaseModel):
    PolicySummary: OrganizationsPolicySummaryModel | None = None
    Content: StrictStr | None = None
