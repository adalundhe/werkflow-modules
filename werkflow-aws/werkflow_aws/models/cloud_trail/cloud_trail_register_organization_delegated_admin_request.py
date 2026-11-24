from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailRegisterOrganizationDelegatedAdminRequest(BaseModel):
    MemberAccountId: StrictStr
