from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerRegisterOrganizationAdminAccountRequest(BaseModel):
    adminAccountId: StrictStr
