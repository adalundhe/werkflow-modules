from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEnableOrganizationAdminAccountRequest(BaseModel):
    AdminAccountId: StrictStr
