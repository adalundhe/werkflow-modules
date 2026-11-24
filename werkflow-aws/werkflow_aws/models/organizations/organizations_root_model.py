from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_policy_type_summary_model import OrganizationsPolicyTypeSummaryModel


class OrganizationsRootModel(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    PolicyTypes: list[OrganizationsPolicyTypeSummaryModel] | None = None
