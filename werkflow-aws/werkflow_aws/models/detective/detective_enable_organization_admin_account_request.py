from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveEnableOrganizationAdminAccountRequest(BaseModel):
    AccountId: StrictStr
