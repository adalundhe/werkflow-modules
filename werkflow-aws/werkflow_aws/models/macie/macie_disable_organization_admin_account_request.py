from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDisableOrganizationAdminAccountRequest(BaseModel):
    adminAccountId: StrictStr
