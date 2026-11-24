from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_policy_type_summary import OrganizationsPolicyTypeSummary


class OrganizationsOrganization(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    FeatureSet: StrictStr | None = None
    MasterAccountArn: StrictStr | None = None
    MasterAccountId: StrictStr | None = None
    MasterAccountEmail: StrictStr | None = None
    AvailablePolicyTypes: list[OrganizationsPolicyTypeSummary] | None = None
