from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableIpamOrganizationAdminAccountRequest(BaseModel):
    DelegatedAdminAccountId: StrictStr
    DryRun: StrictBool | None = None
