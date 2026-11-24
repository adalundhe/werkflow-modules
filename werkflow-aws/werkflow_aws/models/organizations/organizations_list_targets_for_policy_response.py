from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_policy_target_summary import OrganizationsPolicyTargetSummary


class OrganizationsListTargetsForPolicyResponse(BaseModel):
    Targets: list[OrganizationsPolicyTargetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
