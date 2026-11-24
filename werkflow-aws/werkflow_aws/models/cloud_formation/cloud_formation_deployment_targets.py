from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDeploymentTargets(BaseModel):
    Accounts: list[StrictStr] | None = None
    AccountsUrl: StrictStr | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
    AccountFilterType: StrictStr | None = None
