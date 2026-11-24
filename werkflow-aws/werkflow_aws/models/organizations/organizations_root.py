from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_policy_type_summary import OrganizationsPolicyTypeSummary


class OrganizationsRoot(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    PolicyTypes: list[OrganizationsPolicyTypeSummary] | None = None
