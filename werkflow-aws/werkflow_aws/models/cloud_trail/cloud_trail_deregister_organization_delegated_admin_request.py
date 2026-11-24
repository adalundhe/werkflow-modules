from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDeregisterOrganizationDelegatedAdminRequest(BaseModel):
    DelegatedAdminAccountId: StrictStr
