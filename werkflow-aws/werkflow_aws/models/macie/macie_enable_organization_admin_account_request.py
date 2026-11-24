from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieEnableOrganizationAdminAccountRequest(BaseModel):
    adminAccountId: StrictStr
    clientToken: StrictStr | None = None
