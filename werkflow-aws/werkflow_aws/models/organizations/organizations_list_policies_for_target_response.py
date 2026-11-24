from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_policy_summary_model import OrganizationsPolicySummaryModel


class OrganizationsListPoliciesForTargetResponse(BaseModel):
    Policies: list[OrganizationsPolicySummaryModel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
